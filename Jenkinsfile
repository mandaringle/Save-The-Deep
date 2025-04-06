pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("mandaringle/save-the-deep:${env.BUILD_ID}", ".")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    dockerHubCredentials = credentials('dockerhub-auth')
                    docker.withRegistry("https://index.docker.io/v1/", dockerHubCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
        failure {
            echo 'Failed to build and push Docker image!'
        }
    }
}