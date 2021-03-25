FROM python:3.8

COPY /datasette/docker/requirements/ /tmp/requirements/
COPY /datasette/docker-entrypoint.sh /app/
COPY /datasette/ /app/
