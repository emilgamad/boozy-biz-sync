"""Boozy Biz Sync Store"""
import requests
import config
import json
import serializer

def biz_store_create_product(product):
    biz_store_product_id = 0
    biz_store_product = serializer.remove_all_ids_from_product(product)

    url = "{}products.json".format(config.BIZ_STORE_DOMAIN)
    print(url)
    response = requests.post(url=url, json=biz_store_product)
    if response.status_code == 200:
        biz_store_product_id = response['product']['id']
    return biz_store_product_id

def biz_store_set_item_level(biz_store_inventory_item_id, serialized_product_item_levels):
    pass
