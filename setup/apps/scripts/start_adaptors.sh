#/bin/sh

ADAPTORS_PATH="/adaptors"



for fl in "$ADAPTORS_PATH"/*.py
do
    if [ -f "$fl" ];then
        pm2 start "$fl"
    fi
done

