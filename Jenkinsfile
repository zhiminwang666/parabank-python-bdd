pipeline {
  agent any
    options {
    timestamps()
  }

  environment {
    HEADLESS = "true"
    VENV = ".venv"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Show Tools') {
      steps {
        bat 'where python'
        bat 'python --version'
        bat 'where git'
        bat 'git --version'
      }
    }

    stage('Setup venv + deps') {
      steps {
        bat """
          if not exist %VENV% (
            python -m venv %VENV%
          )
          %VENV%\\Scripts\\python -m pip install --upgrade pip
          %VENV%\\Scripts\\pip install -r requirements.txt
        """
      }
    }

    stage('Run Tests') {
      steps {
        bat """
          %VENV%\\Scripts\\pytest --alluredir=allure-results
        """
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'allure-results/**', fingerprint: true

      allure([
        includeProperties: false,
        jdk: '',
        results: [[path: 'allure-results']]
      ])
    }
  }
}
