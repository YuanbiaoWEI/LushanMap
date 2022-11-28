pipeline {
  agent any
//  {
//    docker{
//      label 'docker-registry'
//      image 'python:3.9'
//    }
//  }
  
  stages{
    stage('Build'){
      steps{
        // sh 'python --version'
        sh 'docker build -t lushanmap_test:1.0 .'
        sh 'docker images'
        sh 'docker run -di -p 8000:8000 -v /home/LushanMap:/home lushanmap_test:1.0'
      }
    }
  }
}
