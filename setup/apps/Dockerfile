FROM python:3.8.2-slim-buster

WORKDIR /usr/share/apps/scripts
COPY ./scripts/  .
RUN pip install confluent-kafka \
    && pip install requests
