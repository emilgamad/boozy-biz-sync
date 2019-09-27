"""Google subscription service"""
from google.cloud import pubsub_v1
import config

class GoogleSubscriptionService():

    def __init__(self):
        self.subscriber = pubsub_v1.SubscriberClient.from_service_account_json('secrets.json')
        self.subscription_name = config.GCP_SUB_NAME

    def run(self):
        def callback(message):
            print(message.data)
            message.ack()

        self.subscriber.subscribe(self.subscription_name, callback)
