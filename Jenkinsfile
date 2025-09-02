pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = "corpsbliss"
        DOCKERHUB_CREDENTIALS = credentials('docker-hub')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/corpsbliss/kafka-elk.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh """
                  docker build -t $DOCKERHUB_REPO/userservice:latest ./user_service
                  docker build -t $DOCKERHUB_REPO/orderservice:latest ./order_service
                """
            }
        }

        stage('Push Docker Images') {
            steps {
                sh """
                  echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                  docker push $DOCKERHUB_REPO/userservice:latest
                  docker push $DOCKERHUB_REPO/orderservice:latest
                """
            }
        }
    }
}
