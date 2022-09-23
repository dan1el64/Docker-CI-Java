# temp container to clone github
FROM ubuntu as TEMP_GIT
#ENV TOKEN_GITHUB
#ENV REPODEI_GITHUB
ARG TOKEN_GITHUB
ARG REPODEI_GITHUB
#Install git
RUN apt-get update        
RUN apt-get install -y git
RUN mkdir /home/sampleTest     
RUN cd /home/sampleTest       
RUN git clone -b main https://${TOKEN_GITHUB}:x-oauth-basic@${REPODEI_GITHUB} /home/sampleTest 
#Set working directory
WORKDIR /home/sampleTest


# temp container to build using gradle
FROM gradle:7.4.1 AS TEMP_BUILD_IMAGE
ENV APP_HOME=/app/
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY --from=TEMP_GIT /home/sampleTest $APP_HOME  
USER root
RUN chown -R gradle .
# RUN gradle runDev 
RUN gradle build 

# actual container
FROM openjdk:11
ENV ARTIFACT_NAME=deitest-0.0.1-SNAPSHOT.jar
ENV APP_HOME=/app
RUN mkdir -p $APP_HOME/config
COPY --from=TEMP_BUILD_IMAGE $APP_HOME/build/libs/${ARTIFACT_NAME} /app/${ARTIFACT_NAME}
COPY --from=TEMP_BUILD_IMAGE $APP_HOME/config/application.properties /app/config/application.properties
EXPOSE 8080
ENTRYPOINT ["java", "-jar","-Dspring.config.location=file:/app/config/application.properties","/app/deitest-0.0.1-SNAPSHOT.jar"]
