"""Config file for boozy-biz-sync"""
import os

PROJECT_NAME = os.getenv('GOOGLE_CLOUD_PROJECT')

if PROJECT_NAME is None or "staging" in PROJECT_NAME:
    MAIN_STORE = [
        {"API_KEY": "8b2c2f515ff17743be71ae5b479297c9"},
        {"PASSWORD": "7ae645b889c0708b6747bb5dbd31e382"},
        {"SHARED_SECRET": "73d853860d4a6c52ff045d5226a2406e"},
        {"DOMAIN": "letsboozy-staging.myshopify.com/admin/api/2019-07/"}]
else:
    MAIN_STORE = [
        {"API_KEY": "f3ec4f3a98c7f27aff8d470053d6242e"},
        {"PASSWORD": "171df07b59a4faba3a2575aadd0a1940"},
        {"SHARED_SECRET": "e48a122231e37ed46cff2ec1442e96fb"},
        {"DOMAIN": "letsboozy.myshopify.com/admin/api/2019-07/"}]

MAIN_STORE_DOMAIN = "https://{}:{}@{}".format(
    MAIN_STORE[0]['API_KEY'],
    MAIN_STORE[1]['PASSWORD'],
    MAIN_STORE[3]['DOMAIN'])


BIZ_STORE = [
    {"API_KEY": "8bb186724efe3d240b039b5a888391eb"},
    {"PASSWORD": "e8feb211776e5c80af55dcbbaf34605a"},
    {"SHARED_SECRET": "474a553c2ae21c03456b2b5527127aab"}]

BIZ_STORE_DOMAIN = "https://{}:{}boozy-biz.myshopify.com/admin/api"\
    "/2019-07/".format(BIZ_STORE[0]['API_KEY'], BIZ_STORE[1]['PASSWORD'])
