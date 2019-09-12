"""Config file for boozy-biz-sync"""
import os

PROJECT_NAME = os.getenv('GOOGLE_CLOUD_PROJECT')

if PROJECT_NAME is None or "staging" in PROJECT_NAME:
    pass


MAIN_STORE = [
    "API_KEY":
]
