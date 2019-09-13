"""Boozy Biz Sync Store"""
import requests
import pyrebase
import config
import json
from manager import Manager
from datetime import datetime


class Store():
    """Setters"""
    def __init__(self):
        self.manager = Manager()
        self.firebase = pyrebase.initialize_app(config.FIREBASE_CONFIG)
        auth = self.firebase.auth()
        self.user = auth.sign_in_with_email_and_password(
            config.FIREBASE_ADMIN, config.FIREBASE_PASSWORD)

    def start_sync_store_listener_service(self):
        db = self.firebase.database()
        db.child("syncStore").stream(self.stream_handler)

    def stream_handler(self, message):
        print(message["event"]) # put
        print(message["path"]) # /-K7yGTTEp7O549EzTYtI
        print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
