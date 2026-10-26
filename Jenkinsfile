pipeline{
    agent any{
        stages{
            stage('Run selenium test'){
                steps{
                    sh'pip3 install -r requirements.txt'
                    sh'sleep 5'
                    sh'python3 -m pytest test_selenium.py'

                }
            }
            stage('Build Docker Image'){
                steps{
                    echo 'Building Docker image...'
                    sh'docker build -t dedeepya2001/selenium-app .'
                }
            }
            stage('Login to Docker Hub'){
                steps{
                    echo 'Logging in to Docker Hub...'
                    credentials {
                        usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')
                    }
        
                }
            }

            stage('Push Docker Image'){
                steps{
                    echo 'Pushing Docker image...'

                    sh'docker push dedeepya2001/selenium-app'

                }
            }
            stage('Deploy to Kubernetes'){
                steps{
                    echo 'Deploying to Kubernetes...'
                    sh'kubectl apply -f deployment.yaml'
                    sh'kubectl apply -f service.yaml'
                }
            }
            stage('Verify Deployment'){
                steps{
                    echo 'Verifying deployment...'
                    sh'kubectl get pods'
                    sh'kubectl get services'
                }
            }
        post{
            success{
                echo 'Pipeline completed successfully!'
            }
            failure{
                echo 'Pipeline failed!'
            }  
        }
    }
}
}