pipeline {
    agent any

    environment {
        DOCKER_USER = 'Keerthi'
        DOCKER_PASS = 'Keerthi@88'
        DOCKER_IMAGE = 'keerthi/student-app'
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
                    // Using shell commands instead of docker.build()
                    sh """
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh """
                    docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}
                    docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                    docker push ${DOCKER_IMAGE}:latest
                    docker logout
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl set image deployment/student-app student-app=${DOCKER_IMAGE}:${BUILD_NUMBER} --record
                kubectl rollout status deployment/student-app
                """
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
