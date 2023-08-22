import utilities
import json
import time
from kafka import KafkaProducer


def start_streaming():
    producer = KafkaProducer(bootstrap_servers=['localhost:9091', 'localhost:9092', 'localhost:9093'], api_version=(3,3,1), value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    end_time = time.time() + 120 # pour 2 minutes

    while time.time() < end_time:
        results = utilities.get_random_person_data('https://randomuser.me/api/')
        data = utilities.retrieve_best_format_data(results)
        print(data)
        producer.send("random_persons_infos",data)
        time.sleep(10)


if __name__=="__main__":
    start_streaming()