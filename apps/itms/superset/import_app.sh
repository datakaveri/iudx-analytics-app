#/bin/bash

DB_URL=$DB_URL

# ITMS DB
superset set-database-uri --database_name ITMS --uri "$DB_URL"


for fl in ./*.yaml
do
    if [ -f "$fl" ];then
        superset import-datasources -p $fl
    fi
done


for fl in ./*.json
do
    if [ -f "$fl" ];then
        superset import-dashboards -p $fl
    fi
done


