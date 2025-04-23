pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонируем репозиторий
                git 'https://github.com/Minimaxind/shaper.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Установка зависимостей
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестов
                sh 'python -m unittest discover'
            }
        }
    }

    post {
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
