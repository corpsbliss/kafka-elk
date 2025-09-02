FROM jenkins/jenkins:lts-jdk11

USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    git \
    ca-certificates \
    apt-transport-https \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------
# Install Docker CLI (works on ARM too)
# ---------------------------------------------------
RUN curl -fsSL https://get.docker.com | sh

# ---------------------------------------------------
# Install kubectl (pinned version for ARM64)
# ---------------------------------------------------
ENV KUBE_VERSION=v1.30.0
RUN curl -LO "https://dl.k8s.io/release/${KUBE_VERSION}/bin/linux/arm64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# ---------------------------------------------------
# Install Helm (pinned version)
# ---------------------------------------------------
ENV HELM_VERSION=v3.14.4
RUN curl -LO https://get.helm.sh/helm-${HELM_VERSION}-linux-arm64.tar.gz \
    && tar -zxvf helm-${HELM_VERSION}-linux-arm64.tar.gz \
    && mv linux-arm64/helm /usr/local/bin/helm \
    && rm -rf linux-arm64 helm-${HELM_VERSION}-linux-arm64.tar.gz

# ---------------------------------------------------
# Install Terraform (pinned version for ARM64)
# ---------------------------------------------------
ENV TERRAFORM_VERSION=1.6.6
RUN curl -fsSL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_arm64.zip -o terraform.zip \
    && unzip terraform.zip \
    && mv terraform /usr/local/bin/ \
    && rm terraform.zip

USER jenkins
