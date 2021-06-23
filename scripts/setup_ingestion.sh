#/bin/bash

PROJECT_ROOT="$PWD/../"
export PROJECT_ROOT=$PROJECT_ROOT

echo "[1] AQM  [2] ITMS  [3] Both"
read appname


export CONFIG_FILE="$PROJECT_ROOT/configs/config.json"


docker network create analytics-net

docker-compose \
    -f $PROJECT_ROOT/setup/zookeeper/docker-compose.yml \
    -f $PROJECT_ROOT/setup/kafka/docker-compose.yml \
    up -d zook kafka 




if [[ $appname -eq 1 ]]
then
    export TOPICS_FILE="$PROJECT_ROOT/apps/aqm/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/aqm/adaptors/"
    docker-compose \
        -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
        up -d kafka kafkainit adaptors
fi

if [[ $appname -eq 2 ]]
    export TOPICS_FILE="$PROJECT_ROOT/apps/itms/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/itms/adaptors/"
    docker-compose \
        -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
        up -d kafka kafkainit adaptors
fi


if [[ $appname -eq 3]]

    export TOPICS_FILE="$PROJECT_ROOT/apps/aqm/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/aqm/adaptors/"
    export ADAPTOR_NAME="AQM"
    docker-compose \
        -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
        up -d kafka kafkainit adaptors

    export TOPICS_FILE="$PROJECT_ROOT/apps/itms/kafka/topics.json"
    export ADAPTORS_PATH="$PROJECT_ROOT/apps/itms/adaptors/"
    export ADAPTOR_NAME="ITMS"
    docker-compose \
        -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
        up -d kafka kafkainit adaptors
then
fi
