from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def log_to_kafka(user_id, action, timestamp):
    message = {
        "user_id": user_id,
        "action": action,
        "timestamp": timestamp
    }
    producer.send("logs", value=message)
