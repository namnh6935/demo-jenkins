pipeline {
  agent {label 'build-dev'}
  environment {
    ENV = "dev"
    NODE = "build-dev"
    DOCKER_HUB = "namhn89"
    DOCKERHUB_CREDENTIALS=credentials('dockerhub')
  }

  stages {
    stage('Build Image') {
      agent {
        node {
          label "$NODE"
        }
      }

      environment {
        TAG = sh(returnStdout: true, script: "git rev-parse -short=10 HEAD | tail -n +2").trim()
      }

      steps {
        sh "docker build -t fastapi-$ENV:latest ."
        sh "docker images"
        sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB --password-stdin"
        sh "docker tag fastapi-$ENV:latest $DOCKER_HUB/fastapi:$TAG"
        sh "docker push $DOCKER_HUB/fastapi:$TAG"
        sh "docker rmi -f $DOCKER_HUB/fastapi:$TAG"
        sh "docker rmi -f fastapi-$ENV:latest"
      }
    }
  }
}