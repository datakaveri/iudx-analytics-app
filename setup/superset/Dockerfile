FROM amancevice/superset:latest

ENV TZ Asia/Kolkata
RUN apt install tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
