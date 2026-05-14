pipeline{
    agent any

    stages{
        stage('Build docker image'){
            steps{
                bat 'docker build -t flask-demo-app .'
            }
        }
        stage('Start Docker container'){
            steps{
                bat 'docker rm -f flask-container || true'
                bat 'docker run -d -p 5000:5000 --name flask-container flask-demo-app'
            }
        }
    }
}
