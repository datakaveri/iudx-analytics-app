# Store your configs here

1. `config.json` - The IUDX RMQ subscriber configuration params

A sample config is as shown 
``` 
{
    "<adaptor-id>: {
        "queueName": "<queue name as returned by iud subscription api call>",
        "routingKey": "<resource id of your interest",
        "username": "<username as returned by iudx subscription api call>",
        "password": "<password as returned by iudx subscription api call>"
    }
}
```


2. `backend_config.sh` - Druid db URI
``` 
#/bin/bash
export DB_URL="druid://broker:8082/druid/v2/sql"
```
