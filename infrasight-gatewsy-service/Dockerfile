FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/gateway

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./gateway.jar
ENTRYPOINT [ "java", "-jar", "gateway.jar" ]
