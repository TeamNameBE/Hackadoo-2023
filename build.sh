export COMPOSE_PROJECT_NAME=gazette
COMPOSE_FILE=docker-compose.yml
docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME up -d --build
# docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME restart nginx  # Sometimes the connection between nginx and web fails
