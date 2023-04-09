#!/bin/bash -x

./manage.py collectstatic --clear --noinput; ./manage.py migrate; gunicorn hackadoo.wsgi:application --bind 0.0.0.0:8000 --timeout 300