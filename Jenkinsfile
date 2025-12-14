pipeline {
    agent none
    options { timestamps() }

    stages {

        stage('Checkout SCM') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Build') {
            agent any
            steps {
                echo "Building project #${BUILD_NUMBER}"
            }
        }

        stage('Test (Unit tests in Docker)') {
            agent any
            steps {
                bat '''
                docker run --rm ^
                  -v %CD%:/app ^
                  -w /app ^
                  python:3.11-slim ^
                  python -m unittest discover
                '''
            }
        }

        stage('Build & Push Docker Image') {
            agent any
            steps {
                script {
                    def dockerHubUser = 'volodimirbabak'
                    def repoName = 'python-lab4'

                    docker.withRegistry('', 'dockerhub-creds') {
                        def image = docker.build("${dockerHubUser}/${repoName}:${env.BUILD_NUMBER}")
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }
    }

    post {
        success { echo "Pipeline completed successfully!" }
        failure { echo "Pipeline failed!" }
    }
}
