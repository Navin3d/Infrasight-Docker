FROM amazoncorretto:20-alpine

WORKDIR /usr/infrasight/backend/auth

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./auth.jar
ENTRYPOINT [ "java", "-jar", "auth.jar" ]
