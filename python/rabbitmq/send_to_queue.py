#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # Durable again, see consume_queue.py for more info

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',               # this is the default exchange which this the 'direct' type
                      routing_key='task_queue',  # This is the queue name
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent, so to requeue when Rabbit crashes
                      ))
print(" [x] Sent %r" % message)
connection.close()