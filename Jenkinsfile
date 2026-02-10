pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Setup') {
      steps {
        bat 'python -m venv .venv'
        bat '.\\.venv\\Scripts\\pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        bat '.\\.venv\\Scripts\\pytest --alluredir=allure-results'
      }
    }
    stage('Archive') {
      steps {
        archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
      }
    }
  }
}
