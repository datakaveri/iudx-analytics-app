declare -a names
declare -a ids
i=1
for d in $(docker ps --format "{{.Names}}")
do
    names[i++]=$d
done
i=1
for d in $(docker ps -a -q)
do
    ids[i++]=$d
done
for((i=1;i<=${#names[@]};i++))
do
    version=1
    while true
    do
      if [[ "$(docker images -q iudx/${names[i]}:v$version)" == "" ]]; then
        echo iudx/${names[i]}:v$version": Version doesn't exist, creating image now"
        docker commit ${ids[i]} iudx/${names[i]}:v$version
        break
        else
           echo iudx/${names[i]}:v$version": Version already exists. Skipping."
      fi
      ((version++))
    done
    echo "===================================="
done
