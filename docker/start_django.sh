#!/bin/bash -x

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

./manage.py collectstatic --clear --noinput; ./manage.py migrate; gunicorn hackadoo.wsgi:application --bind 0.0.0.0:8000 --timeout 300