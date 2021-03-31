#/bin/bash

PROJECT_ROOT="$PWD/../"

source "$PROJECT_ROOT/configs/backend_config.sh"

export APPS_PATH="$PROJECT_ROOT/apps/aqm/superset/"

docker network create analytics-net

(cd ../setup/superset/ \
    && docker-compose up -d)

(docker exec -it superset_superset_1 superset-init)

(docker exec -it superset_superset_1 bash -c "cd /apps && sh import_app.sh")
