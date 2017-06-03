import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'


from pyspark import SparkContext #Spark

from pyspark.streaming import StreamingContext #    Spark Streaming

from pyspark.streaming.kafka import KafkaUtils #    Kafka

import json

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 60)

kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming', {'twitter':1})

parsed = kafkaStream.map(lambda v: json.loads(v[1]))

parsed.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()

authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])

author_counts = authors_dstream.countByValue()
author_counts.pprint()

author_counts = authors_dstream.countByValue()
author_counts.pprint()

ssc.start()