#/bin/bash

docker network rm analytics-net

(cd ../setup/zookeeper/ \
    && docker-compose down -v)

(cd ../setup/kafka/ \
    && docker-compose down -v)

(cd ../setup/apps/ \
    && docker-compose down -v)
