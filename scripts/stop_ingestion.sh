#/bin/bash

PROJECT_ROOT="$PWD/../"
export PROJECT_ROOT=$PROJECT_ROOT

docker network rm analytics-net


docker-compose \
    -f $PROJECT_ROOT/setup/zookeeper/docker-compose.yml \
    -f $PROJECT_ROOT/setup/kafka/docker-compose.yml \
    -f $PROJECT_ROOT/setup/apps/docker-compose.yml \
    down -v
