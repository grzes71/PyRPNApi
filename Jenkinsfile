pipeline {
    agent {
        label "windows"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev-1', url: 'https://github.com/grzes71/PyRPNApi.git'
            }
        }
        stage('Dependencies') {
            steps {
                withPythonEnv('Python3') {
                    bat label:'deps', script: 'pip.exe install -e .[dev]'
		        }
            }
        }
        stage('Build') {
            steps {
                withPythonEnv('Python3') {
                    bat label:'wheel', script:'python setup.py bdist_wheel'
		        }
            }
        }
        stage('Test') {
            steps {
                withPythonEnv('Python3') {
                    bat label:'pytest', script:'python setup.py test'
                    junit 'junit.xml'
                    cobertura autoUpdateHealth: false, autoUpdateStability: false,  coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', 
                              failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', 
                              maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, 
                              sourceEncoding: 'ASCII', zoomCoverageChart: false
                }
            }
        }
        stage('Lint') {
            steps {
                withPythonEnv('Python3') {
                    bat label:'pylint', 
                        script:'''pylint --exit-zero --rcfile=.pylintrc \
                        --output-format=parseable --fail-under=3 pyrpnapi \
                        --msg-template=\"{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}\" \
                        > pylint.log
                        '''  
                    recordIssues tool: pyLint(pattern: 'pylint.log'),
                                 enabledForFailure: true, aggregatingResults: true
                }
            }
        }
        stage('Documentation') {
            steps {
                withPythonEnv('Python3') {
                    bat label:'sphinx', script:'python setup.py build_sphinx'
                }
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, 
                keepAll: false, reportDir: 'build/sphinx/html', reportFiles: 'index.html', 
                reportName: 'Docs', reportTitles: 'API Documentation'])
                
            }
        }
        stage('Deploy') {
            steps {
                archiveArtifacts artifacts: 'dist/**/*.whl', followSymlinks: false
            }
        }
    }
}
