FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/capture

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./capture.jar
ENTRYPOINT [ "java", "-jar", "capture.jar" ]
