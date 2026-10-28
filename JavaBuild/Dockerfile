# Supply a locally built artifact from an authorized source.
# Authentication tokens must never be passed as Docker ARG or embedded in clone URLs.
FROM eclipse-temurin:11-jre-alpine
WORKDIR /app
COPY artifacts/app.jar /app/app.jar
USER 10001
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "-Dspring.config.location=file:/app/config/application.properties", "/app/app.jar"]
