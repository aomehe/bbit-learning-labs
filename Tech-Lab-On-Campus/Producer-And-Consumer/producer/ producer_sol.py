
import pika
import os
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str):   
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        print("The routing key is ", self.routing," and the exchange name is ", self.exchange_name)
        self.setupRMQConnection()
        self.publishOrder()

    def setupRMQConnection(self):
      
        message = "Output text"

        ## Connecting to RabbitMQ service/ Set-up Connection
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establishing Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        if self.exchange_name is None:
            self.exchange = self.channel.exchange_declare(exchange="Exchange Name")
        
        self.publishOrder(message)

    def publishOrder(self, message: str):
        # Publishing To An Exchange
        self.channel.basic_publish(
            exchange = self.exchange_name,
            routing_key = self.routing_key,
            body = message)
        # Closing Channel and Connection
        self.channel.close()
        self.connection.close()






        
