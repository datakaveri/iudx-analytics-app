FROM nikolaik/python-nodejs

WORKDIR /usr/share/apps/scripts
COPY ./scripts/  ./scripts/
COPY ./adaptor/ ./adaptor/
RUN pip install confluent-kafka \
    && pip install requests \
    && npm install pm2 -g \
    && pip install poetry \
    && pip install pika \
    && pip install retry \
    && cd adaptor \
    && pip install .\
    && pip install python-dateutil\
    && pip install pytz\
    && pip install wheel\
    && pip install pandas\
    && pip install schedule
    
CMD bash -c "./scripts/start_adaptors.sh && pm2 logs"
