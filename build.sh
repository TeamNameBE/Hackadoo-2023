export COMPOSE_PROJECT_NAME=gazette
COMPOSE_FILE=docker-compose.yml
docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME up -d --build
docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME exec web poetry run python3 manage.py migrate --noinput
docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME exec web poetry run python3 manage.py collectstatic --no-input --clear
docker-compose -f docker/$COMPOSE_FILE -p $COMPOSE_PROJECT_NAME restart nginx  # Sometimes the connection between nginx and web fails
