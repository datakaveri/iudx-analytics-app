FROM ubuntu:18.04 
RUN apt-get update -y &&  apt-get install wget -y
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc
RUN chmod +x mc
RUN ./mc --help
ARG ALIAS=default
ENV ALIAS $ALIAS

ARG ENDPOINT_URI=default
ENV ENDPOINT_URI $ENDPOINT_URI

ARG USERNAME=default
ENV USERNAME $USERNAME

ARG PASSWORD=default
ENV PASSWORD $PASSWORD

ARG BUCKET_NAME=default
ENV BUCKET_NAME $BUCKET_NAME

WORKDIR .
ADD docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]