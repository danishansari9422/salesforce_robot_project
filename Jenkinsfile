pipeline {
    agent any

    stages {
        // Checkout stage: Fetch the code from Git repository
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
    sleep 30
        // Run Robot Framework Tests
        stage('Run Robot Framework Tests') {
            steps {
                sleep 15
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

        // // Post Actions: Clean up workspace after execution
        // stage('Post Actions') {
        //     steps {
        //         cleanWs() // Clean workspace after execution
        //     }
        //}
    }
}
