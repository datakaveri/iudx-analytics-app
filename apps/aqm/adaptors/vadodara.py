from adaptor.Adaptor import Adaptor
import json
import sys
import requests

adaptor_id = "vadodara-aqm-ingestion"
config_path = "/config.json"

lookup = {}


def user_callback(body):
    global lookup
    x = json.loads(body)
    ks = list(x.keys())
    for k in ks:
        x["latitude"] =  lookup[x["id"]]["latitude"]
        x["longitude"] =  lookup[x["id"]]["longitude"]
        if (isinstance(x[k], dict) and "instValue" in  list(x[k].keys())):
            x[k] = x[k]["instValue"]
    body = json.dumps(x).encode('utf-8')
    return body


def main():
    
    config = {}
    with open(config_path, "r") as f:
        config = json.load(f)[adaptor_id]

    grp_id = "vmc.gov.in/ae95ac0975a80bd4fd4127c68d3a5b6f141a3436/rs.iudx.org.in/vadodara-env-aqm"
    api = "https://api.catalogue.iudx.org.in/iudx/cat/v1/relationship?id=xx&rel=resource"
    api = api.replace("xx", grp_id)
    data = requests.get(api).json()["results"]
    for d in data:
        lookup[d["id"]] = {}
        coords = d["location"]["geometry"]["coordinates"]
        lookup[d["id"]]["latitude"] = coords[1]
        lookup[d["id"]]["longitude"] = coords[0]
    print(lookup)


    adaptor_obj = Adaptor()
    adaptor_obj.set_host("databroker.iudx.org.in")
    adaptor_obj.set_port(24567)
    adaptor_obj.set_vhost("IUDX")

    adaptor_obj.set_username(config["username"])
    adaptor_obj.set_password(config["password"])
    adaptor_obj.set_queuename(config["queueName"])
    adaptor_obj.set_routingkey(config["routingKey"])

    adaptor_obj.set_bootstrap_server("kafka:19092")
    adaptor_obj.create_producer()
    adaptor_obj.set_kafkatopic("vadodara-aqm")

    adaptor_obj.set_user_callback(user_callback)

    print("Subscribing")
    adaptor_obj.subscribe()

if __name__ == "__main__":
    main()
