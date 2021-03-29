from adaptor.Adaptor import Adaptor
import pytest
import json

def user_callback(body):
    data = json.loads(body)
    print(data)
    return json.dumps(data).encode("utf-8")


def test_adaptor():
    print("Starting this test")
    adaptor_obj = Adaptor()
    adaptor_obj.set_bootstrap_server("localhost:9092")
    adaptor_obj.set_host("localhost")
    adaptor_obj.set_port(5672)
    adaptor_obj.set_vhost("/")
    adaptor_obj.set_queuename("adaptor-test")
    adaptor_obj.set_routingkey("test")
    adaptor_obj.set_kafkatopic("itms-live")
    adaptor_obj.set_user_callback(user_callback)
    print("Subscribing")
    adaptor_obj.subscribe()
    
