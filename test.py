from kafka import KafkaConsumer


bootstrap_servers = ['localhost:9092']
topicName = 'test'
consumer = KafkaConsumer(
    topicName,
    group_id = 'group1',
    bootstrap_servers = bootstrap_servers)

for msg in consumer:
    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
    print(f'{msg.topic} {msg.value}')

