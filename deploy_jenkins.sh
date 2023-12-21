docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  --name jenkins \
  -v ./data:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17