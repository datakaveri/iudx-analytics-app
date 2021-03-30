#/bin/bash

PROJECT_ROOT="/home/rraks/Work/gitrepos/iudx-analytics-app"

export TOPICS_FILE="$PROJECT_ROOT/apps/aqm/kafka/topics.json"
export ADAPTORS_PATH="$PROJECT_ROOT/apps/aqm/adaptors/"
export CONFIG_FILE="$PROJECT_ROOT/scripts/configs/config.json"


docker network create analytics-net

(cd ../setup/zookeeper/ \
    && docker-compose up -d)

(cd ../setup/kafka/ \
    && docker-compose up -d)

# TODO: Find alternative.
sleep 10

(cd ../setup/apps/ \
    && docker-compose up kafkainit \
    && docker-compose up -d adaptors)

