from confluent_kafka import Producer
import pika
import urllib.parse
import json
import time
from retry import retry

class Adaptor():
    """Abstract class for adaptor.
    """

    def __init__(self):
        """init function
        Args:
        to do: Initialize with default parameters    
        """
        self.username: str = ""
        self.password: str = ""
        self.host: str = "localhost"
        self.vhost: str = "vhost"
        self.port : int = 9092
        self.queue_name: str = "queue_name"
        self.routing_key: str = "routing_key"
        self.kafka_topic: str = "kafka_topic"
        self.user_callback = None

        self.bootstrap_server = ''

        self.producer = None

    """RMQ Config Getter and Setter functions
    """
    def create_producer(self):
        self.producer = Producer({'bootstrap.servers': self.bootstrap_server})

    def set_bootstrap_server(self, server: str):
        self.bootstrap_server = server
        return self

    def set_username(self, username):
        self.username = urllib.parse.quote_plus(username)
        return self
    
    def set_password(self, password):
        self.password = password
        return self
    
    def set_host(self, host):
        self.host = host
        return self
    
    def set_port(self, port):
        self.port = port
        return self
    
    def get_rmqconfig(self):
        return self
    

    """Kafka Config Getter and Setter functions
    """
    def set_vhost(self, vhost):
        self.vhost = vhost
        return self
    
    def set_queuename(self, queue_name):
        self.queue_name = queue_name
        return self
    
    def set_routingkey(self, routing_key):
        self.routing_key = routing_key
        return self
    
    def set_kafkatopic(self, kafka_topic):
        self.kafka_topic = kafka_topic
        return self

    def get_kafkaconfig(self):
        return self
    
    """ Streaming subscription
    """
    @retry(pika.exceptions.AMQPConnectionError, delay=1, jitter=(1, 3))
    def subscribe(self):
        while(True):
            if (self.username == "" and self.password == ""):
                connection = pika.BlockingConnection(pika.URLParameters(f'amqp://{self.host}:{self.port}'))
            else:
                connection = pika.BlockingConnection(pika.URLParameters(f'amqps://{self.username}:{self.password}@{self.host}:{self.port}/{self.vhost}'))
            channel = connection.channel()
            channel.basic_consume(queue=self.queue_name, on_message_callback=self.default_callback, auto_ack=True)
            try:
                channel.start_consuming()
            except KeyboardInterrupt:
                print("Stopping Connection")
                channel.stop_consuming
                connection.close()
            except pika.exceptions.ConnectionClosedByBroker:
                print("Restarting Connection")
                continue


    """ Kafka publish callback """
    def delivery_report(self, err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))


    """RMQ Callback
    """
    def default_callback(self, channel, method, properties, body):
        data = self.user_callback(body)
        self.publish(self.kafka_topic, data)
        

    def set_user_callback(self, callback):
        self.user_callback = callback

    def publish(self, kafka_topic, data):
        self.producer.poll(0)
        self.producer.produce(kafka_topic, data, callback=self.delivery_report)

    """Run
    """
    def run(self):
        while(True):
            time.sleep(1) 

