pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Compila la imagen Docker
                    sh "docker build -t black_box_sodimac ."
                }
            }
        }

        stage('Run Tests in Docker Container') {
            steps {
                script {
                    // Ejecuta las pruebas en el contenedor
                    sh "docker run black_box_sodimac"
                }
            }
        }
    }
}
