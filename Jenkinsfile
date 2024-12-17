pipeline {
    agent any

    stages {
        // Checkout stage: Fetch the code from Git repository
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        // Run Robot Framework Tests
        stage('Run Robot Framework Tests') {
            steps {
                // Execute Robot Framework test
                bat 'robot Tests/remote_login.robot'
            }
        }

        // Post Actions: Clean up workspace after execution
        stage('Post Actions') {
            steps {
                cleanWs() // Clean workspace after execution
            }
        }
    }
}
