"""Config file for boozy-biz-sync"""
import os

PROJECT_NAME = str(os.getenv('GOOGLE_CLOUD_PROJECT'))

if "bzy-biz-sync-stg" in PROJECT_NAME:

    MAIN_STORE = [
        {"API_KEY": "f3ec4f3a98c7f27aff8d470053d6242e"},
        {"PASSWORD": "171df07b59a4faba3a2575aadd0a1940"},
        {"SHARED_SECRET": "e48a122231e37ed46cff2ec1442e96fb"},
        {"DOMAIN": "letsboozy.myshopify.com/admin/api/2019-07/"}]

    # Staging Values
    MAIN_LOCATIONS_LIST = {
        "MAIN_STORE_MAKATI_HUB" : 6956482671,
        "MAIN_STORE_QC_HUB" : 7124451439,
        "MAIN_STORE_ALABANG_HUB" : 15657533551}

elif PROJECT_NAME == "None" or "boozy-biz-sync" in PROJECT_NAME:
    MAIN_STORE = [
        {"API_KEY": "8b2c2f515ff17743be71ae5b479297c9"},
        {"PASSWORD": "7ae645b889c0708b6747bb5dbd31e382"},
        {"SHARED_SECRET": "73d853860d4a6c52ff045d5226a2406e"},
        {"DOMAIN": "letsboozy-staging.myshopify.com/admin/api/2019-07/"}]

    #Prod Values
    MAIN_LOCATIONS_LIST = {
        "MAIN_STORE_MAKATI_HUB" : 42445973,
        "MAIN_STORE_QC_HUB" : 13981909067,
        "MAIN_STORE_ALABANG_HUB" : 15035039819}

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


BIZ_STORE_MAKATI_HUB = 33229733968
BIZ_STORE_QC_HUB = 33992900688
BIZ_STORE_ALABANG_HUB = 33992802384

BIZ_LOCATIONS_LIST = {
    "BIZ_STORE_MAKATI_HUB": 33229733968,
    "BIZ_STORE_QC_HUB": 13981909067,
    "BIZ_STORE_ALABANG_HUB": 33992802384
}

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyAQbrpEylB7Q4U6qtVV6byuCHXRHVxtIUY",
    "authDomain": "boozy-biz-sync-staging-848f4.firebaseapp.com",
    "databaseURL": "https://boozy-biz-sync-staging-848f4.firebaseio.com",
    "projectId": "boozy-biz-sync-staging-848f4",
    "storageBucket": "",
    "messagingSenderId": "796210140291",
    "appId": "1:796210140291:web:29cec974f13901444e77b6"}

FIREBASE_ADMIN = "emil.gamad@boozy.ph"
FIREBASE_PASSWORD = "boozy-biz-sync-staging"

GCP_TOPIC_NAME = "projects/bzy-biz-sync-stg/topics/boozy-biz-sync"

GCP_SUB_NAME = 'projects/bzy-biz-sync-stg/subscriptions/testsub'
