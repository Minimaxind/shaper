pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонируем репозиторий
                git 'https://github.com/Minimaxind/shaper.git'  // Замените на ваш URL
            }
        }
        stage('Install Dependencies') {
            steps {
                // Установка зависимостей, если у вас есть requirements.txt
                script {
                    if (fileExists('requirements.txt')) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found, skipping dependency installation.'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестов
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed!'
        }
    }
}
