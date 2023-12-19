FROM amazoncorretto:21-alpine

WORKDIR /usr/infrasight/backend/discovery

# COPY . .
# RUN ./mvnw clean package -DskipTests

# ENTRYPOINT [ "java", "-jar", "/target/*.jar" ]

COPY ./target/*.jar ./discovery.jar
ENTRYPOINT [ "java", "-jar", "discovery.jar" ]
