kafka-elk/
│
├── user_service/
│   ├── userservice.py
│   ├── Dockerfile
│
├── order_service/
│   ├── orderservice.py
│   ├── Dockerfile
│
├── helm/
│   └── log-generator/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│
├── terraform/
│   └── main.tf     # (for minikube bootstrap, optional)
│
└── Jenkinsfile
