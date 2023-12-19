FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/presentation

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./presentation.jar
ENTRYPOINT [ "java", "-jar", "presentation.jar" ]
