import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer
from kafka.cluster import ClusterMetadata


topic_name = "test"


class Producer(threading.Thread):
    daemon = True

    def run(self):
        print("Running Producer")
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        while True:
            producer.send(topic_name, b"test")
            producer.send(topic_name, b"Hola, mundo!")
            time.sleep(1)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        print("Running Consumer")
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe([topic_name])

        for message in consumer:
            print (message)


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()




    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()