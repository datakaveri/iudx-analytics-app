#/bin/bash

docker network rm analytics-net

(cd ../setup/druid/ \
    && docker-compose down -v)


