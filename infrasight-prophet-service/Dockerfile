FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/prophet

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./prophet.jar
ENTRYPOINT [ "java", "-jar", "prophet.jar" ]
