@Library('jenkins_lib')_
pipeline {
  agent {label 'slave'}
  environment { 
   	DEB_COMPONENT = 'cdap'
	DEB_ARCH = 'amd64'
	DEB_POOL = 'gvs-dev-debian/pool/c'
	ARTIFACT_SRC1 = './cdap/**/target'
	ARTIFACT_SRC2 = './cdap-ambari-service/target'
	ARTIFACT_DEST1 = 'gvs-dev-debian/pool/c'
	SONAR_PATH_CDAP = './cdap'
	SONAR_PATH_APP_ARTIFACTS_DRE = './app-artifacts/dre'
	SONAR_PATH_APP_ARTIFACTS_HYDRATOR_PLUGINS = './app-artifacts/hydrator-plugins'
	SONAR_PATH_APP_ARTIFACTS_MRDS = './app-artifacts/cdap-mrds'
	SONAR_PATH_APP_ARTIFACTS_MMDS = './app-artifacts/mmds'
	SONAR_PATH_APP_ARTIFACTS_AFE = './app-artifacts/auto-feature-engineering'
	SONAR_PATH_SECURITY_EXTN = './security-extensions/cdap-security-extn'  
	}
  stages {
    stage("Define Release version"){
      steps {
      script {
        versionDefine()
        }
      }
    }
    
	stage('Build') {
	  steps {
	    script {
		sh"""
		git clean -xfd  && \
		git submodule foreach --recursive git clean -xfd && \
		git reset --hard  && \
		git submodule foreach --recursive git reset --hard && \
		git submodule update --remote && \
		git submodule update --init --recursive --remote && \
		export MAVEN_OPTS="-Xmx3056m -XX:MaxPermSize=128m" && \
		mkdir build  && \
		cd build  && \
		cmake ..  && \
		make  && \
		cd .. && \
		cd cdap-ambari-service && \
		./build.sh && \
		cd .. && \
		cd cdap && \
		mvn clean install -Dmaven.test.skip=true -Dcheckstyle.skip && \
		cd .. && \
		mvn clean install -Dmaven.test.skip=true -Dcheckstyle.skip=true -B -am -pl cdap/cdap-api -P templates && \
		mvn clean install -Dmaven.test.skip=true -Dcheckstyle.skip=true -B -am -f cdap/cdap-app-templates -P templates && \
                cd ${env.WORKSPACE}/app-artifacts/auto-metadata-service && \
                mvn clean install -Dcheckstyle.skip=true && \
                mkdir -p build && \
                cd build && \
                cmake .. && \
                make metadatasync_rpm && \
                cd ../../../
		"""
	}}}

	stage("RPM PUSH"){
	  steps{
	    script{
	    sh ''
	  rpm_push( env.buildType, '${WORKSPACE}/app-artifacts/auto-metadata-service/', 'ggn-dev-rpms/metadatasync/' )
	  rpm_push( env.buildType, '${WORKSPACE}/cdap/**/target', 'ggn-dev-rpms/cdap-build' )
	  rpm_push( env.buildType, '${WORKSPACE}/cdap-ambari-service/target', 'ggn-dev-rpms/cdap-build' )
	  rpm_push( env.buildType, '${WORKSPACE}', 'ggn-dev-rpms/cdap-build' )
	  deb_push(env.buildType, env.ARTIFACT_SRC1, env.ARTIFACT_DEST1 )
          deb_push(env.buildType, env.ARTIFACT_SRC2, env.ARTIFACT_DEST1 ) 
    }}}
  }
	
post {
       always {
          reports_alerts('target/checkstyle-result.xml', 'target/surefire-reports/*.xml', '**/target/site/cobertura/coverage.xml', 'allure-report/', 'index.html')
     	  slackalert('jenkins-cdap-alerts')
       }
    }

}
