# IUDX Analytics App

An production ready demo analytics application framework built over IUDX.
Some of the demo dashboards can be found [here](#dashboards).


## Architecture
This app demonstrates the implementation  of a scalable and big-data ready architecture
based on IUDX datasources based completely on open-source components.
<p align="center">
<img src="./docs/diagrams/Architecture.png">
</p>

The components involved are
- *RMQ-Kafka Adaptor* - The main consumer of IUDX data. Publishes into Kafka for consumption of the database and analytic blocks.
- [*Kafka*](https://kafka.apache.org/) - Application internal event streaming. Primarily serves as a log store for database ingestion and publishing of processed data from the analytic blocks.
- [*Druid*](https://druid.apache.org/) - The workhorse of this application. It's high ingestion rate and fast queries make it an ideal candidate for high ingestion rate datasources (like GTFS).
- [*Zookeeper*](https://zookeeper.apache.org/) - Cenralized server for maintaining configurations and synchronizations.
- [*Superset*](https://superset.apache.org/) - Visualization engine with large scale distribution capabilities.

## Setup
Setting this application will require multiple servers and of different configurations
depending on the scale and number of datasources.
- Druid:  Minimum: 2CPUs and 16GB RAM, single node deployments may need multiple vms for different datasources depending on the retention policy
- Zookeeper:  Minimum: 1CPU and 2GB RAM
- Kafka:  Minimum: 2CPUs and 8GB RAM
- Superset:  Minimum: 2CPUs and 8GB RAM

### Setup order
Zookeeper -> Kafka -> Druid -> Adaptors -> Superset -> Apps

Build necessary docker images 
`cd ./scripts/` 
`./build_all.sh`

Usual deployments will have 
1. Ingestion - Zookeeper + Kafka + Druid + Adaptors in one VM
2. Consumption - Superset + Apps in another VM.


### Ingestion setup
This setup takes care of setting the ingestion pipeline, i.e, bringing up Zookeeper, Kafka, Druid and setting up the adaptors.
You will need access to streaming data from IUDX.
This involves registration and consent from providers of the datasources.
Please contact [us](mailto:rakshit.ramesh@datakaveri.org?subject=[Analytics%20App%20Support]%20Request%20Access) for support on this.

1. Add a configuration file in `./configs/config.json` with IUDX subscription secrets
2. Execute the ingestion script `cd ./scripts && ./setup_ingestion.sh`
2. Execute the database script `cd ./scripts && ./setup_db.sh`

### Consumption setup
This setup takes care of bringing up superset configured to the datasources ingested previously.

1. Add the DB url in `./configs/backend_config.sh`
2. `cd ./scripts/`
3. `./setup_app.sh`

### Fine tuning
  
##### Zookeeper fine tuning
1. `cd ./setup/zookeeper`
2. Edit zookeeper settings as required in `./setup/zookeeper/docker-compose.yml` and 
   `docker-compose up -d`

##### Kafka fine tuning
1. Ensure `zookeeper` is visible in the docker network
2. `cd ./setup/kafka/`
3. Edit configuration in `docker-compose.yml` such as zookeeper service name and address, and `KAFKA_ADVERTISED_LISTENERS` for visibility outside the container.  
4. `docker-compose up -d`


##### Druid fine tuning
1. Ensure `zookeeper` is visible in the docker network
2. `cd ./setup/druid`
3. Edit `./setup/druid/environment` for common java properties
4. Edit `./setup/druid/*.env` for druid component specific jvm properties 
5. Edit `./setup/druid/docker-compose.yml` with proper env variables, network settings etc.
6. Bring up different druid services in different vms if required (especially `historical`) or in a single vm 
   `docker-compose up -d`
```
Check the group ownership of all configuration files, environment files and `storage` folder. Make sure they are not root.
```



## <a name="dashboards"></a> Live Dashboards

- Air Quality monitoring 
  - [Pune](https://analytics.iudx.org.in/r/47)
  - [Vadodara](https://analytics.iudx.org.in/r/49)
  - [Varanasi](https://analytics.iudx.org.in/r/48)

- Intelligent Transit Management System 
  - [Surat](https://analytics.iudx.org.in/r/50) (Coming soon)


## Future works
1. Apache airflow based orchestration
2. Fully configurable apps (frontend) based on single configuration file
3. Swarm/Kubernets based setup


## Support
Please contact [us](mailto:rakshit.ramesh@datakaveri.org?subject=[Analytics%20App%20Support]%20Request%20Access) for any support.
