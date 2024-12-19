pipeline {
    agent any

    stages {
        // Checkout stage: Fetch the code from Git repository
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        // Run Selenium Test
        stage('Run Selenium Test') {
            steps {
                script {
                    bat 'python Resources/test_script.py' 
                }
            }
        }

        // Run Robot Framework Tests
        stage('Run Robot Framework Tests') {
            steps {
                // Execute Robot Framework test
                bat 'python -m robot Tests/remote_login.robot'
            }
        }

        // Archive Test Results
        stage('Archive Test Results') {
            steps {
                archiveArtifacts artifacts: '**/log.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/report.html', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/output.xml', allowEmptyArchive: true
            }
        }

        // // Optional Post Actions: Clean up workspace after execution
        // stage('Post Actions') {
        //     steps {
        //         cleanWs() // Clean workspace after execution
        //     }
        // }
    }
}
