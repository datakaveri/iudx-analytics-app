#/bin/bash

DB_URL=$DB_URL

# AQM DB
superset set-database-uri --database_name aqm --uri "$DB_URL"


# Pune AQM
superset import-datasources -p ./pune-aqm-datasource.yaml
superset import-dashboards -p ./pune-aqm-dashboard.json


# Varanasi AQM
superset import-datasources -p ./varanasi-aqm-datasource.yaml
superset import-dashboards -p ./varanasi-aqm-dashboard.json


# Vadodara AQM
superset import-datasources -p ./vadodara-aqm-datasource.yaml
superset import-dashboards -p ./vadodara-aqm-dashboard.json

