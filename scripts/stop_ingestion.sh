#/bin/bash

docker network rm analytics-net

(cd ../setup/zookeeper/ \
    && docker-compose down)

(cd ../setup/kafka/ \
    && docker-compose down)

(cd ../setup/apps/ \
    && docker-compose down)
