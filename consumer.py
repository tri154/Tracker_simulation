from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'tracking',
    bootstrap_servers='localhost:9092',
    group_id='visualization',  # Set a group ID
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',  # Read from the beginning if no offset is committed
    enable_auto_commit=True
)

print("Listening for messages on topic 'tracking'...")

# Poll and print incoming messages
for message in consumer:
    print("Received:", message.value)
    print(type(message.value))
