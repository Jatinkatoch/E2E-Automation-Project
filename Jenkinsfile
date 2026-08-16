// pipeline {
//     agent any

//     parameters {
//         choice(
//             name: 'HEADLESS',
//             choices: ['true', 'false'],
//             description: 'Run Playwright in headless or headed mode'
//         )
//     }

//     environment {
//         PODMAN = 'C:\\Users\\asus\\AppData\\Local\\Programs\\Podman\\podman.exe'
//         PROJECT = 'C:\\Users\\asus\\Desktop\\Ecommerce-Website\\Ecommerce-Website\\TechStore'
//     }

//     stages {

//         stage('Check Podman') {
//             steps {
//                 bat '''
//                 "%PODMAN%" --version
//                 "%PODMAN%" ps
//                 '''
//             }
//         }

//         stage('Start Application') {
//             steps {
//                 bat '''
//                 "%PODMAN%" start ecommerce-app
//                 '''
//             }
//         }

//         stage('Wait 10 Seconds') {
//             steps {
//                 powershell 'Start-Sleep -Seconds 10'
//             }
//         }

//         stage('Run Playwright Tests') {
//             steps {
//                 bat '''
//                 "%PODMAN%" run --rm ^
//                 --network ecommerce-network ^
//                 -e HEADLESS=%HEADLESS% ^
//                 -v "%PROJECT%\\automation\\videos:/automation/videos" ^
//                 -v "%PROJECT%\\automation\\reports:/automation/reports" ^
//                 -v "%PROJECT%\\automation\\traces:/automation/traces" ^
//                 -v "%PROJECT%\\automation\\screenshots:/automation/screenshots" ^
//                 localhost/automationimage:latest
//                 '''
//             }
//         }

//         stage('Copy Test Reports') {
//             steps {
//                 bat '''
//                 if not exist reports mkdir reports

//                 xcopy /E /I /Y "%PROJECT%\\automation\\reports" reports
//                 xcopy /E /I /Y "%PROJECT%\\automation\\screenshots" reports\\screenshots
//                 xcopy /E /I /Y "%PROJECT%\\automation\\videos" reports\\videos
//                 xcopy /E /I /Y "%PROJECT%\\automation\\traces" reports\\traces
//                 '''
//             }
//         }

//     }

//     post {
//         always {
//         script {
//             if (fileExists('reports')) {
//                 archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true

//                 publishHTML(target: [
//                     allowMissing: true,
//                     alwaysLinkToLastBuild: true,
//                     keepAll: true,
//                     reportDir: 'reports',
//                     reportFiles: 'report.html',
//                     reportName: 'Playwright HTML Report'
//                 ])
//             }
//         }
//     }

//     success {
//         echo 'Playwright execution completed successfully.'
//     }

//     failure {
//         echo 'Playwright execution failed.'
//     }
//     }
// }
pipeline {

    agent any


    options {

        timestamps()

        disableConcurrentBuilds()

        buildDiscarder(
            logRotator(
                numToKeepStr: '10'
            )
        )
    }


    parameters {

        choice(
            name: 'HEADLESS',
            choices: [
                'true',
                'false'
            ],
            description: 'Playwright execution mode'
        )
    }


    environment {

        PODMAN = "podman"

        NETWORK = "ecommerce-network"

        APP_IMAGE = "localhost/ecommerce-app"

        TEST_IMAGE = "localhost/playwright-tests"

        CONTAINER = "ecommerce-app"

        BUILD_TAG = "${BUILD_NUMBER}"
    }


    stages {


        stage('Checkout') {

            steps {

                echo "Checking source code"

                checkout scm

            }
        }



        stage('Environment Validation') {

            steps {

                sh '''
                podman --version
                git --version
                '''
            }
        }



        stage('Create Network') {

            steps {

                sh '''
                podman network exists ${NETWORK} ||
                podman network create ${NETWORK}
                '''
            }
        }




        stage('Build Application Image') {

            steps {

                echo "Building application image"


                sh '''
                podman build \
                -t ${APP_IMAGE}:${BUILD_TAG} \
                -t ${APP_IMAGE}:latest \
                .
                '''
            }
        }




        stage('Deploy Application') {

            steps {


                sh '''
                podman rm -f ${CONTAINER} || true


                podman run -d \
                --name ${CONTAINER} \
                --network ${NETWORK} \
                -p 5000:5000 \
                ${APP_IMAGE}:${BUILD_TAG}

                '''
            }
        }




        stage('Health Check') {

            steps {


                sh '''

                sleep 10


                curl --fail http://localhost:5000 || exit 1

                '''

            }
        }




        stage('Build Automation Image') {

            steps {


                sh '''

                cd automation


                podman build \
                -t ${TEST_IMAGE}:${BUILD_TAG} \
                -t ${TEST_IMAGE}:latest \
                .

                '''

            }
        }




        stage('Run Playwright Tests') {

            steps {


                sh '''

                podman run --rm \
                --network ${NETWORK} \
                -e HEADLESS=${HEADLESS} \
                -v $(pwd)/automation/reports:/automation/reports \
                -v $(pwd)/automation/screenshots:/automation/screenshots \
                -v $(pwd)/automation/videos:/automation/videos \
                -v $(pwd)/automation/traces:/automation/traces \
                ${TEST_IMAGE}:${BUILD_TAG}

                '''
            }
        }




        stage('Archive Evidence') {

            steps {


                archiveArtifacts(
                    artifacts:
                    'automation/reports/**,automation/screenshots/**,automation/videos/**,automation/traces/**',
                    allowEmptyArchive:true
                )

            }
        }




        stage('Publish Report') {

            steps {


                publishHTML([

                    allowMissing:false,

                    alwaysLinkToLastBuild:true,

                    keepAll:true,

                    reportDir:'automation/reports',

                    reportFiles:'report.html',

                    reportName:'Playwright Report'

                ])

            }
        }

    }



    post {


        always {


            echo "Cleaning containers"


            sh '''

            podman stop ${CONTAINER} || true

            podman rm ${CONTAINER} || true

            '''

        }


        success {

            echo "BUILD SUCCESS"

        }


        failure {

            echo "BUILD FAILED"

        }

    }

}