#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # durable marks queue as persistent so that queues are not lost when
                                                        # Rabbit crashes,
                                                        # Note that if the same queue name had already
                                                        # been created with durable=False, you need to delete it first
                                                        # for this to take effect
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag) ## Since this is a no_ackk=False (see <<ACK>> below)
                                                     ## We need to send ack back to queue after done
                                                     ## If not then there will be TROUBLE !!!!!

channel.basic_qos(prefetch_count=1) # prefetch_count to 1 sends message to worker only when it has finished prev.
                                    # This is to guard against odd/even==>light/heavy tasks situation
                                    # Need to guard against queue build up
channel.basic_consume(callback,
                      queue='task_queue'
                      # ,no_ack=True    # <<ACK>>Don't set to true so that failed messages gets requeued
                    )


channel.start_consuming()


#######



import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] begin")
    # time.sleep(5)
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello'
                      # ,no_ack=True    # Don't set to true so that failed messages gets requeued
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()