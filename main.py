from infrastructure.messaging.producerkafka import producerkafka

class main():

    if __name__ == "__main__":

        kafka_producer = producerkafka('localhost:9093', 'Post.Sale')  

        while True:
            leitura = input("Digite uma mensagem: ")

            kafka_producer.send("mensagem", leitura)

main()