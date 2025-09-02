Run command

docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/ubuntu/.kube:/var/jenkins_home/.kube \
  jenkins-cicd:arm64

Build command

docker buildx build --platform linux/arm64 \
  -t jenkins-cicd:arm64 \
  -f Dockerfile.jenkins . --load

