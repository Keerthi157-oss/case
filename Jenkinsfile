pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jampallykeerthi/student-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Keerthi157-oss/case.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Login and Push to Docker Hub') {
            steps {
                script {
                    // Manual login using username and password
                    sh 'echo "Keerthi@88" | docker login -u jampallykeerthi --password-stdin'

                    // Push the image
                    sh '''
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                    docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/student-app student-app=${DOCKER_IMAGE}:${BUILD_NUMBER} --record
                kubectl rollout status deployment/student-app
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}
