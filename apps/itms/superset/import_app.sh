#/bin/bash

DB_URL=$DB_URL

# ITMS DB
superset set-database-uri --database_name itms --uri "$DB_URL"


# Pune ITMS
superset import-datasources -p ./clean_vehicle.yaml
superset import-datasources -p ./common_eta.yaml
superset import-datasources -p ./common_schedule.yaml
superset import-datasources -p ./grouped_trip_maps.yaml
superset import-datasources -p ./grouped_trip_maps_1.yaml
superset import-datasources -p ./itms_eta.yaml
superset import-datasources -p ./itms_schedule.yaml
superset import-datasources -p ./itms_vehicle.yaml
superset import-datasources -p ./percentage_missed_trips.yaml
superset import-datasources -p ./trip_analysis_line.yaml
superset import-datasources -p ./trip_analysis_pie.yaml
superset import-datasources -p ./trips_offset.yaml
superset import-datasources -p ./trip_time_eta.yaml
superset import-datasources -p ./uncommon_trips.yaml
superset import-datasources -p ./vehicle_heatmap.yaml
superset import-dashboards -p ./pune-itms-dashboard.json
