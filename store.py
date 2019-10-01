"""Boozy Biz Sync Store"""
import requests
import pyrebase
import config
import json
from datetime import datetime


class Store():
    """Setters"""

    def biz_store_get_product_by_title(self, product_title):
        url = "{}product.json?title={}".format(
            config.BIZ_STORE_DOMAIN,
            product_title)
        response = requests.get(url=url)
        if response.status_code == 200:
            product = json.loads(response.text)

            return item_levels['inventory_levels']
        return None
    #     db = self.firebase.database()
    #     db.child("syncStore").stream(self.stream_handler)
    #
    # def stream_handler(self, message):
    #     print(message["event"]) # put
        # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
        # print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
