#/bin/bash

PROJECT_ROOT="$PWD/../"
export PROJECT_ROOT=$PROJECT_ROOT

echo "[1] AQM  [2] ITMS"
read appname

if [[ $appname -eq 1 ]]
then
    export TOPICS_FILE="$PROJECT_ROOT/apps/aqm/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/aqm/adaptors/"
else
    export TOPICS_FILE="$PROJECT_ROOT/apps/itms/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/itms/adaptors/"
fi

export CONFIG_FILE="$PROJECT_ROOT/configs/config.json"


docker network create analytics-net

docker-compose \
    -f $PROJECT_ROOT/setup/zookeeper/docker-compose.yml \
    -f $PROJECT_ROOT/setup/kafka/docker-compose.yml \
    -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
    up -d zook kafka kafkainit adaptors

