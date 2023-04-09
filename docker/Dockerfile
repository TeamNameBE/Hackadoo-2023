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

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

# Trick to copy libs instead of symlinking them
RUN python -m venv --copies /srv/venv
# Install required libs
RUN . /srv/venv/bin/activate \
    && poetry install --only main

ENV PATH /srv/venv/bin:$PATH

EXPOSE 8000

RUN chmod u+x /srv/docker/start_django.sh
CMD /srv/docker/start_django.sh
