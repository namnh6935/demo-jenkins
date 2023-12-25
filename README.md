- [DevOps Training Homework](#devops-training-homework)
  - [Setting up Jenkins](#setting-up-jenkins)
  - [Setup Jenkins pipeline by Jenkinsfile](#setup-jenkins-pipeline-by-jenkinsfile)
  - [Setup agent and node to build, deploy service](#setup-agent-and-node-to-build-deploy-service)
    - [Credential by secret text, secret password, secret user](#credential-by-secret-text-secret-password-secret-user)
    - [Result](#result)
# DevOps Training Homework
## Setting up Jenkins
Use a script to deploy jenkins container
```
sh deploy_jenkins.sh
```
Jenkins will ask you for `admin` password. You can retrieve it by running:
```
docker exec Jenkins_Docker cat /var/jenkins_home/secrets/initialAdminPassword
```
## Setup Jenkins pipeline by Jenkinsfile
## Setup agent and node to build, deploy service
Create an agent to build image and push image to docker registry
![agent](./images/agent.png)
### Credential by secret text, secret password, secret user
Use credential jenkins(secret file, text, user, password) to secure the password, user, environment variables and database name in project
![credential](./images/credential.png)

### Result
The result of Jenskin pipeline
![result](./images/result.png)
