pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Smoke Tests') {
            steps {
                bat 'pytest -m smoke --headless -v'
            }
        }
        stage('Regression Suite') {
            steps {
                bat 'pytest --headless -v --html=reports/report.html'
            }
        }
    }
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}