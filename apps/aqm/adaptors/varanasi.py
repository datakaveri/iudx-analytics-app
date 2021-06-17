from adaptor.Adaptor import Adaptor
import json
import requests

adaptor_id = "varanasi-aqm-ingestion"
config_path = "/config.json"

grp_id = "varanasismartcity.gov.in/62d1f729edd3d2a1a090cb1c6c89356296963d55/rs.iudx.org.in/varanasi-env-aqm"
api = "https://api.catalogue.iudx.org.in/iudx/cat/v1/relationship?id=xx&rel=resource"
api = api.replace("xx", grp_id)
data = requests.get(api).json()["results"]
lookup = {}

for d in data:
    lookup[d["id"]] = {}
    coords = d["location"]["geometry"]["coordinates"]
    lookup[d["id"]]["latitude"] = coords[1]
    lookup[d["id"]]["longitude"] = coords[0]


def user_callback(body):
    global lookup
    x = json.loads(body)
    ks = list(x.keys())
    for k in ks:
        x["latitude"] =  lookup[x["id"]]["latitude"]
        x["longitude"] =  lookup[x["id"]]["longitude"]
        if (isinstance(x[k], dict) and "avgOverTime" in  list(x[k].keys())):
            x[k] = x[k]["avgOverTime"]
    body = json.dumps(x).encode('utf-8')
    return body


def main():
    
    config = {}
    with open(config_path, "r") as f:
        config = json.load(f)[adaptor_id]


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
    adaptor_obj.set_kafkatopic("varanasi-aqm")

    adaptor_obj.set_user_callback(user_callback)

    print("Subscribing")
    adaptor_obj.subscribe()

if __name__ == "__main__":
    main()
