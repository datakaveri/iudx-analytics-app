FROM python:3.8.2-slim-buster

WORKDIR /usr/share/apps/kafkainit
COPY ./scripts/  .
RUN pip install confluent-kafka
# ENTRYPOINT python3 ./create_topics.py
