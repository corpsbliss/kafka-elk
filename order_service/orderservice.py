import logging
import random
import time
from datetime import datetime

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [OrderService] %(message)s"
)
logger = logging.getLogger("order-microservice")

ACTIONS = [
    "Order placed",
    "Order confirmed",
    "Order shipped",
    "Order delivered",
    "Order cancelled",
    "Payment received",
    "Refund initiated"
]

LEVELS = [logging.INFO, logging.WARNING, logging.ERROR]

def generate_order_log():
    """Generate a random order service log entry."""
    action = random.choice(ACTIONS)
    level = random.choice(LEVELS)
    order_id = f"ORD-{random.randint(1000, 9999)}"
    customer_id = f"CUST-{random.randint(100, 999)}"
    return f"{action} | order_id={order_id} | customer_id={customer_id}", level

if __name__ == "__main__":
    logger.info("Starting OrderService log generator...")

    while True:
        msg, level = generate_order_log()
        logger.log(level, msg)
        # Faster/slower pace
        time.sleep(random.uniform(0.05, 0.3))

