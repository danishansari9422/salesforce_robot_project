pipeline {
    agent any

    stages {
        print("Hello World")
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

        stage('Archive Test Results') {
            steps {
                archiveArtifacts artifacts: '**/log.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/report.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/output.xml', allowEmptyArchive: true
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
