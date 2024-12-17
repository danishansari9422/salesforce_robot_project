pipeline {
    agent any

    stages {
        // Install Robot Framework
        stage('Install Robot Framework') {
            steps {
                // Install Robot Framework and its dependencies
                bat 'pip install --upgrade pip'
                bat 'pip install robotframework'
                bat 'pip install robotframework-remote'
            }
        }

    stages {
        // Checkout stage: Fetch the code from Git repository
        stage('Checkout Code') {
            steps {
                checkout scm
                sleep time: 30, unit: 'SECONDS'  // Sleep for 30 seconds
            }
        }

        // Run Robot Framework Tests
        stage('Run Robot Framework Tests') {
            steps {
                sleep time: 15, unit: 'SECONDS'  // Sleep for 15 seconds
                // Execute Robot Framework test
                bat 'python -m robot Tests/remote_login.robot'
            }
        }

        stage('Archive Test Results') {
            steps {
                archiveArtifacts artifacts: '**/log.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/report.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/output.xml', allowEmptyArchive: true
            }
        }

        // Optional Post Actions: Clean up workspace after execution
        // Uncomment if needed
        // stage('Post Actions') {
        //     steps {
        //         cleanWs() // Clean workspace after execution
        //     }
        // }
    }
}
