"""Google Publishing Client Service"""
import config
from google.cloud import pubsub_v1


class GooglePublishMessageService():
    def __init__(self, message):
        self.publisher = pubsub_v1.PublisherClient.from_service_account_json('secrets.json')
        self.topic_name = config.GCP_TOPIC_NAME
        self.message = str(message).encode()

    def run(self):
        self.publisher.publish(self.topic_name, self.message)
