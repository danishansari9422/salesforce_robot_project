pipeline {
    agent any

    environment {
        // Set up any environment variables you need
    }

    stages {
        // Checkout stage: Fetch the code from Git repository
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        // Set up the Python environment
        stage('Set Up Python Environment') {
            steps {
                // This is where you set up Python, check the version, and install dependencies
                bat 'python --version'  // Check Python version on Windows (use 'sh' for Linux/macOS)
                bat 'pip install --upgrade pip' // Optional: Update pip to the latest version
                bat 'pip install -r requirements.txt'  // Install dependencies from requirements.txt
            }
        }

        // Run Robot Framework Tests
        stage('Run Robot Framework Tests') {
            steps {
                // Command to execute Robot Framework tests
                bat 'robot tests/remote_login.robot'
            }
        }

        // Post Actions: Clean up workspace, notifications, etc.
        stage('Post Actions') {
            steps {
                cleanWs() // Clean workspace after execution
            }
        }
    }
}
