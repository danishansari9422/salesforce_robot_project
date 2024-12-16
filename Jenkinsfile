pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/danishansari9422/salesforce_robot_project.git' // Replace with your GitHub repo URL
            }
        }
        stage('Set Up Python Environment') {
            steps {
                script {
                    // Install Python and Robot Framework dependencies
                    sh 'python -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt' // Ensure Robot Framework and any other dependencies are installed
                }
            }
        }
        stage('Run Robot Framework Tests') {
            steps {
                script {
                    // Execute Robot Framework tests
                    sh './venv/bin/salesforce_robot_project/Tests/remote_login.robot' // Adjust with the correct path to your test files
                }
            }
        }
    }
    post {
        always {
            // Clean up or send notifications after the tests
            cleanWs()
        }
    }
}
