#/bin/sh

ADAPTORS_PATH=$ADAPTORS_PATH



for fl in "$ADAPTORS_PATH"/*.py
do
    if [ -f "$fl" ];then
        pm2 start "$fl"
    fi
done

