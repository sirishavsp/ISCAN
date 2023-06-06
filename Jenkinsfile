pipeline {
    agent any

    stages {
        stage('Pull Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sirishavsp/ISCAN.git'
            }
        }

        stage('Install Packages') {
            steps {
                sh 'pip3 install Flask==2.1.0 python-hcl2==3.0.0 networkx==2.6.2 fuzzywuzzy==0.18.0 radon==4.1.0 tabulate==0.8.9 requests==2.26.0'
            }
        }

        stage('Run Scanner') {
            steps {
                sh 'python3 main.py'
            }
        }
        
        stage('Generate Report') {
            steps {
                sh 'python3 codeScanner/ReportGenerator/report.py'
                sh 'mv codeScanner/ReportGenerator/reports codeScanner/reports'  // Move the reports directory to the correct location
                stash includes: 'codeScanner/reports/**', name: 'report'  // Adjust the stash path
            }
        }
        
        stage('Start Flask Server') {
            steps {
                sh 'python3 -m flask run'
            }
        }
        
        stage('Publish Report') {
            steps {
                unstash 'report'
                step([$class: 'JUnitResultArchiver', testResults: 'codeScanner/reports/*.xml'])  // Adjust the testResults path
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'codeScanner/reports', reportFiles: 'index.html', reportName: 'IAC Code Scanner Report'])
            }
        }
    }
}
