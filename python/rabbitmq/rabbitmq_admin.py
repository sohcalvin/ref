import pika



pika_conn_params = pika.ConnectionParameters(
    host='localhost', port=5672,
    credentials=pika.credentials.PlainCredentials('guest', 'guest'),
)
pika_conn_params = pika.URLParameters('amqp://guest:guest@localhost:5672/')
connection = pika.BlockingConnection(pika_conn_params)

queue_names = ["rpc-job_matcher", "rpc-career_level_classifier", "xyourqueu"]
for qn in queue_names :
    channel = connection.channel()
    queue = channel.queue_declare(
        queue=qn, durable=True,
        exclusive=False, auto_delete=False
    )
    print("{} : {}".format(qn, queue.method.message_count))

connection.close()

# "amqp://5b2417953756eeaa38bf178884525fd7:e17fbe69802ba94b444223d41a24d2d0@10.11.17.179:5672/production"