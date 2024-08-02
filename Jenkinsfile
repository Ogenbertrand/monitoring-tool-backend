pipeline {
    agent any
    environment{
        DOCKER_IMAGE = "location-app"
        DOCKER_TAG = "latest"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build "${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside("${DOCKER_IMAGE}:${DOCKER_TAG}") {
                        sh 'python3 -m pytest -v --junit-xml test-reports/results.xml'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}