#/bin/bash

PROJECT_ROOT="$PWD/../"
export PROJECT_ROOT=$PROJECT_ROOT


echo "[1] AQM  [2] ITMS"
read appname

if [[ $appname -eq 1 ]]
then
    export SPEC_PATH="$PROJECT_ROOT/apps/aqm/druid/"
else
    export SPEC_PATH="$PROJECT_ROOT/apps/itms/druid/"
fi

docker network create analytics-net

(cd ../setup/druid/ \
    && docker-compose -f docker-compose-create.yml up --no-start)

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
