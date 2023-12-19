FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/server

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./server.jar
ENTRYPOINT [ "java", "-jar", "server.jar" ]
