FROM python:3.9

COPY /datasette/docker/requirements/ /tmp/requirements/
COPY /datasette/docker-entrypoint.sh /app/
COPY /datasette/ /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /tmp/requirements/base.txt
EXPOSE 90

RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]