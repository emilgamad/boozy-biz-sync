"""Boozy Biz Sync Manager"""
import requests
import config
import json


def main_store_get_product_by_id(product_id):
    url = "{}products/{}.json".format(
        config.MAIN_STORE_DOMAIN,
        product_id)
    print(url)
    response = requests.get(url=url)
    if response.status_code == 200:
        product = json.loads(response.text)
        return product['product']
    return None

def main_store_get_variant_by_id(variant_id):
    url = "{}variants/{}.json".format(
        config.MAIN_STORE_DOMAIN,
        variant_id)
    print(url)
    response = requests.get(url=url)
    if response.status_code == 200:
        variant = json.loads(response.text)
        return variant['variant']
    return None

def main_store_get_item_levels_by_id(item_inventory_id):
    url = "{}inventory_levels.json?inventory_item_ids={}".format(
        config.MAIN_STORE_DOMAIN,
        item_inventory_id)
    response = requests.get(url=url)
    if response.status_code == 200:
        item_levels = json.loads(response.text)
        return item_levels['inventory_levels']
    return None

def biz_store_get_product_by_id(product_id):
    url = "{}products/{}.json".format(
        config.BIZ_STORE_DOMAIN,
        product_id)
    print(url)
    response = requests.get(url=url)
    if response.status_code == 200:
        product = json.loads(response.text)
        return product['product']
    return None

def biz_store_get_product_by_title(product_title):
    url = "{}product.json?title={}".format(
        config.BIZ_STORE_DOMAIN,
        product_title)
    response = requests.get(url=url)
    if response.status_code == 200:
        product = json.loads(response.text)
        return product['products'][0]
    return None

def biz_store_get_variant_by_id(variant_id):
    url = "{}variants/{}.json".format(
        config.BIZ_STORE_DOMAIN,
        variant_id)
    print(url)
    response = requests.get(url=url)
    if response.status_code == 200:
        variant = json.loads(response.text)
        return variant['variant']
    return None

def biz_store_get_item_levels_by_id(item_inventory_id):
    url = "{}inventory_levels.json?inventory_item_ids={}".format(
        config.BIZ_STORE_DOMAIN,
        item_inventory_id)
    response = requests.get(url=url)
    if response.status_code == 200:
        item_levels = json.loads(response.text)
        return item_levels['inventory_levels']
    return None
