from adaptor.Adaptor import Adaptor
import json
import requests

adaptor_id = "surat-itms-ingestion"
config_path = "./config.json"

grp_id = "suratmunicipal.org/6db486cb4f720e8585ba1f45a931c63c25dbbbda/rs.iudx.org.in/surat-itms-realtime-info/surat-itms-live-eta"


def user_callback(body):
    x = json.loads(body)
    ks = list(x.keys())
    try:
        x["latitude"] =  x['location']["coordinates"][1]
        x["longitude"] =  x['location']["coordinates"][0]
        x.pop("location")
    except Exception as e:
        print(e)

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
    adaptor_obj.set_kafkatopic("surat-itms-live")

    adaptor_obj.set_user_callback(user_callback)

    print("Subscribing")
    adaptor_obj.subscribe()

if __name__ == "__main__":
    main()