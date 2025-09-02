import logging
import random
import time
import threading
from datetime import datetime

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("dummy-microservice")

MESSAGES = [
    "User logged in",
    "User logged out",
    "Payment processed",
    "Payment failed",
    "Item added to cart",
    "Item removed from cart",
    "Order placed",
    "Order cancelled",
    "Inventory updated",
    "Database connection slow",
    "Cache miss",
    "Cache hit",
    "API request timeout",
    "Service unavailable"
]

LEVELS = [logging.INFO, logging.WARNING, logging.ERROR]

def generate_log():
    """Generate a random log entry."""
    message = random.choice(MESSAGES)
    level = random.choice(LEVELS)
    user_id = random.randint(1000, 9999)
    trace_id = f"trace-{random.randint(100000, 999999)}"
    return f"{message} | user_id={user_id} | trace_id={trace_id}", level

def log_spammer(rate_per_sec: int):
    """Continuously generate logs at given rate."""
    interval = 1.0 / rate_per_sec
    while True:
        msg, level = generate_log()
        logger.log(level, msg)
        time.sleep(interval)

if __name__ == "__main__":
    logger.info("Starting high-throughput log generator...")

    # Change this to increase/decrease rate
    logs_per_sec = 500  

    # Use multiple threads if you want >1000 logs/sec
    threads = 4  
    per_thread_rate = logs_per_sec // threads

    for _ in range(threads):
        t = threading.Thread(target=log_spammer, args=(per_thread_rate,))
        t.daemon = True
        t.start()

    # Keep main thread alive
    while True:
        time.sleep(1)

