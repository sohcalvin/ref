
from kafka.cluster import ClusterMetadata


topic_name = "test"

cm = ClusterMetadata(bootstrap_servers='localhost:9092')
for i in cm.topics() :
    print(i)
