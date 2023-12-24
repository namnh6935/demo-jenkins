pipeline {
  agent {label 'build-dev'}
  environment {
    ENV = "dev"
    NODE = "build-dev"
    DOCKER_HUB = "namhn89"
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    POSTGRES_USER = "username"
    POSTGRES_DB = "dbname"
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
        sh "docker tag fastapi-$ENV:latest $DOCKER_HUB/fastapi:$ENV"
        sh "docker push $DOCKER_HUB/fastapi:$ENV"
        sh "docker rmi -f $DOCKER_HUB/fastapi:$ENV"
        sh "docker rmi -f fastapi-$ENV:latest"
      }
    }
  stage('Deploy dev') {
      agent {
        node {
          label "$NODE"
        }
      }
      environment {
        TAG = sh(returnStdout: true, script: "git rev-parse -short=10 HEAD | tail -n +2").trim()
      }
      steps {
        sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB --password-stdin"
        sh "docker pull $DOCKER_HUB/fastapi:$ENV"
        sh "docker tag $DOCKER_HUB/fastapi:$ENV fastapi-$ENV:latest"
        // Deploy PostgreSQL using Docker Compose
        sh "docker-compose -f docker-compose.yml up -d postgres"
        // Wait for PostgreSQL to be healthy (customize the command as needed)
        // sh "docker-compose -f docker-compose.yml exec postgres wait-for-it.sh -q --timeout=60 -- pg_isready -U $POSTGRES_USER -d $POSTGRES_DB"
        sh "docker-compose -f docker-compose.yml up -d fastapi-app"
      }
    }
  }
}