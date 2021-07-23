#!/bin/bash
./mc alias set ${ALIAS} ${ENDPOINT_URI} ${USERNAME} ${PASSWORD}
./mc mb ${ALIAS}/${BUCKET_NAME}
./mc mirror --overwrite --remove --watch  postgresbackup/ ${ALIAS}/${BUCKET_NAME}