# Build npm app
FROM node:19.8-slim as npm_builder

WORKDIR /vue

COPY frontend .
RUN npm i
RUN npm run build

# Build production image
FROM python:3.10-bullseye

WORKDIR /srv

RUN apt update && TZ=Etc/UTC DEBIAN_FRONTEND=noninteractive apt install python3-pip netcat libpq-dev tzdata -y

COPY . .
RUN rm -rf frontend/*
COPY --from=npm_builder /vue/dist /srv/frontend/dist

RUN pip install poetry
RUN poetry install --only main

ENTRYPOINT ["poetry", "run", "/srv/docker/entrypoint.sh"]
CMD ["gunicorn", "hackadoo.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "300"]
