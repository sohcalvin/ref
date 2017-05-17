def getRabbitmqQueues(rabbitmq_conn, list_of_queue_names) :
    list_dict = []
    for qn in list_of_queue_names:
        channel = rabbitmq_conn.channel()
        queue = channel.queue_declare(
            queue=qn, durable=True,
            exclusive=False, auto_delete=False
        )
        list_dict.append({ "queue" : qn, "message_count" : queue.method.message_count })
    return list_dict
