#/bin/bash

PROJECT_ROOT="$PWD/../"

export SPEC_PATH="$PROJECT_ROOT/apps/aqm/druid/"

docker network create analytics-net

(cd ../setup/druid/ \
    && docker-compose up -d)


while true; 
curl -XGET http://localhost:8888
retval=$?
do 
  if [ $retval -eq 0 ] ; then
    (cd ../setup/apps/ \
        && docker-compose up druidinit)
    break
  fi
  echo "Druid not up yet"
  sleep 1; 
done



