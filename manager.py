"""Boozy Biz Sync Manager"""
import requests
import config
import json
import math
import time


def biz_store_get_product_by_handle(handle):
    """Gets products by handle"""
    url = "{}products.json?handle={}".format(config.BIZ_STORE_DOMAIN, handle)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    result = json.loads(response.text)
    return result.get('products', None)

def main_store_get_product_by_handle(handle):
    """Gets products by handle"""
    print("main_store_get_product_by_handle", handle)
    url = "{}products.json?handle={}".format(config.MAIN_STORE_DOMAIN, handle)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    result = json.loads(response.text)
    print(result)
    print("Main Store Product ID", result['products'][0]['id'])
    if len(result['products']) > 0:
        return result['products']
    return None


def biz_store_get_all_published_products():
    """Retreives products/s from biz store"""
    count = 0
    all_product_list = []
    url = "{}products/count.json".format(config.BIZ_STORE_DOMAIN)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    count_string = response.content.decode()
    print(count_string)
    count_json = json.loads(count_string)
    count = math.ceil(count_json['count']/250)
    print(count)
    url = "{}products.json?limit=250".format(config.BIZ_STORE_DOMAIN)
    print(url)
    response = requests.get(url)
    for i in range(count+1):
        print(i)
        product_list_string = response.text
        product_list = json.loads(product_list_string)['products']
        all_product_list.extend(product_list)

        link_string = response.headers['link']
        if len(link_string.split(', ')) > 1:
            next_link = link_string.split(', ')[1]
        else:
            next_link = link_string.split(', ')[0]
        start = next_link.find('page_info')+10
        end = next_link.find('>;')
        page_info = next_link[start:end]
        print(page_info)
        response = requests.get(
            "{}products.json?limit=250&page_info={}".format(config.BIZ_STORE_DOMAIN, page_info)
        )
    all_published_product_list = []
    for product in all_product_list:
        if product['published_at'] != None:
            all_published_product_list.append(product)
    return all_published_product_list


def main_store_get_all_published_products():
    """Retreives products/s from biz store"""
    count = 0
    all_product_list = []
    url = "{}products/count.json".format(config.MAIN_STORE_DOMAIN)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    count_string = response.content.decode()
    print(count_string)
    count_json = json.loads(count_string)
    count = math.ceil(count_json['count']/250)
    print(count)
    url = "{}products.json?limit=250".format(config.MAIN_STORE_DOMAIN)
    print(url)
    response = requests.get(url)
    for i in range(count+1):
        print(i)
        product_list_string = response.text
        product_list = json.loads(product_list_string)['products']
        all_product_list.extend(product_list)

        link_string = response.headers['link']
        if len(link_string.split(', ')) > 1:
            next_link = link_string.split(', ')[1]
        else:
            next_link = link_string.split(', ')[0]
        start = next_link.find('page_info')+10
        end = next_link.find('>;')
        page_info = next_link[start:end]
        print(page_info)
        response = requests.get(
            "{}products.json?limit=250&page_info={}".format(config.MAIN_STORE_DOMAIN, page_info)
        )
    all_published_product_list = []
    for product in all_product_list:
        if product['published_at'] != None:
            all_published_product_list.append(product)
    return all_published_product_list


def main_store_get_product_by_id(product_id):
    url = "{}products/{}.json".format(
        config.MAIN_STORE_DOMAIN,
        product_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        product = json.loads(response.text)
        return product['product']
    return None


def main_store_get_product_by_title(product_title):
    url = "{}products.json?handle={}".format(
        config.MAIN_STORE_DOMAIN,
        product_title)
    print("Main Store", url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        product = json.loads(response.text)
        if product['products']:
            return product['products']
    return None


def main_store_get_variant_by_id(variant_id):
    url = "{}variants/{}.json".format(
        config.MAIN_STORE_DOMAIN,
        variant_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        variant = json.loads(response.text)
        return variant['variant']
    return None


def main_store_get_item_levels_by_id(item_inventory_id):
    url = "{}inventory_levels.json?inventory_item_ids={}".format(
        config.MAIN_STORE_DOMAIN,
        item_inventory_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        item_levels = json.loads(response.text)
        return item_levels['inventory_levels']
    return None

def biz_store_get_item_levels_by_id(item_inventory_id):
    url = "{}inventory_levels.json?inventory_item_ids={}".format(
        config.BIZ_STORE_DOMAIN,
        item_inventory_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        item_levels = json.loads(response.text)
        return item_levels['inventory_levels']
    return None


def biz_store_get_product_by_id(product_id):
    url = "{}products/{}.json".format(
        config.BIZ_STORE_DOMAIN,
        product_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        product = json.loads(response.text)
        return product['product']
    return None


def biz_store_get_product_by_title(product_title):
    url = "{}products.json?handle={}".format(
        config.BIZ_STORE_DOMAIN,
        product_title)
    print("Biz Store", url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        product = json.loads(response.text)
        if product['products']:
            return product['products']
    return None


def biz_store_get_variant_by_id(variant_id):
    url = "{}variants/{}.json".format(
        config.BIZ_STORE_DOMAIN,
        variant_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        variant = json.loads(response.text)
        return variant['variant']
    return None


def biz_store_get_item_levels_by_id(item_inventory_id):
    url = "{}inventory_levels.json?inventory_item_ids={}".format(
        config.BIZ_STORE_DOMAIN,
        item_inventory_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        item_levels = json.loads(response.text)
        return item_levels['inventory_levels']
    return None


def biz_store_get_order_by_id(order_id):
    url = "{}orders/{}.json".format(
        config.BIZ_STORE_DOMAIN,
        order_id)
    print(url)
    try:
        response = requests.get(url)
    except:
        time.sleep(10)
        response = requests.get(url)
    if response.status_code == 200:
        order = json.loads(response.text)
        return order['order']
    return None
