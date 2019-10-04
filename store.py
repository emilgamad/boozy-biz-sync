"""Boozy Biz Sync Store"""
import requests
import config
import time
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
    print(serialized_product_item_levels)
    url = "{}inventory_levels/set.json".format(config.BIZ_STORE_DOMAIN)
    print(url)
    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_MAKATI_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_MAKATI_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_MAKATI_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_QC_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_QC_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_QC_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_ALABANG_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_ALABANG_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_ALABANG_HUB ")
        print(str(e))

    return response

def main_store_set_item_level(main_store_inventory_item_id, serialized_product_item_levels):
    print(serialized_product_item_levels)
    url = "{}inventory_levels/set.json".format(config.MAIN_STORE_DOMAIN)
    print(url)
    try:
        payload = {
            "inventory_item_id": main_store_inventory_item_id,
            "location_id": config.MAIN_LOCATIONS_LIST['MAIN_STORE_MAKATI_HUB'],
            "available": serialized_product_item_levels['BIZ_STORE_MAKATI_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_MAKATI_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": main_store_inventory_item_id,
            "location_id": config.MAIN_LOCATIONS_LIST['MAIN_STORE_QC_HUB'],
            "available": serialized_product_item_levels['BIZ_STORE_QC_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_QC_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": main_store_inventory_item_id,
            "location_id": config.MAIN_LOCATIONS_LIST['MAIN_STORE_ALABANG_HUB'],
            "available": serialized_product_item_levels['BIZ_STORE_ALABANG_HUB']
        }
        response = requests.post(url=url, json=payload)
        time.sleep(1)
    except Exception as e:
        print("Error in setting BIZ_STORE_ALABANG_HUB ")
        print(str(e))

    return response
