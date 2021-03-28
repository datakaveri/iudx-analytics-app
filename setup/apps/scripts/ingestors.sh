#/bin/sh

SPEC_PATH="/specs/druid/"
DRUID_URL=$DRUID_URL



for fl in "$SPEC_PATH"/*
do
    if [ -f "$fl" ];then
        ./post-index-task --file "$fl" --url "http://${DRUID_URL}"
    fi
done

