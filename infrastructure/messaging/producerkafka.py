from time import sleep
from json import dumps
from kafka import KafkaProducer

class producerkafka:
    ''' This application able sent data to kafka broker 

     Keyword Arguments:
        server: kafka connection host 
        topic: kafka topic'''

    def __init__(self, server, topic):
        self.server = server
        self.topic = topic
        
        self.producer = KafkaProducer(bootstrap_servers=[self.server],
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))
        
        self.producer.send(self.topic, value = {"mensagem":"connected"})
        sleep(0.1)

    def send(self, key, value):
                   
        self.data = {key: value}
        self.producer.send(self.topic, value = self.data)
        sleep(0.1)