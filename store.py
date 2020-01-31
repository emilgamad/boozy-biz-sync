"""Boozy Biz Sync Store"""
import requests
import config
import time
import serializer
import json


def biz_store_delete_item(biz_store_product_id):
    url = "{}products/{}.json".format(config.BIZ_STORE_DOMAIN, biz_store_product_id)
    print("Deleting", biz_store_product_id)
    response = requests.delete(url)
    if response.status_code == 200:
        return "Deleted {}".format(biz_store_product_id)
    else:
        return "Failed to delete {}".format(biz_store_product_id)


def biz_store_update_product(product):
    product_id = product['product']['id']
    url = "{}products/{}.json".format(config.BIZ_STORE_DOMAIN, product_id)
    print("PUT", url)
    response = requests.put(url=url, json=product)
    if response.status_code == 200:
        return "Updated Biz Store Product ID "+str(json.loads(response.text)['product']['id'])
    else:
        return response.text


def biz_store_create_product(product):
    url = "{}products.json".format(config.BIZ_STORE_DOMAIN)
    response = requests.post(url=url, json=product)
    if response.status_code == 200:
        return "Created Biz Store Product ID "+str(json.loads(response.text)['products']['id'])
    else:
        return json.loads(response.text)


def biz_store_set_item_level(biz_store_inventory_item_id, serialized_product_item_levels):
    url = "{}inventory_levels/set.json".format(config.BIZ_STORE_DOMAIN)
    print(url)
    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_MAKATI_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_MAKATI_HUB']
        }
        print(payload)
        response = requests.post(url=url, json=payload)
        print(response.text)
    except Exception as e:
        time.sleep(5)
        response = requests.post(url=url, json=payload)
        print("Error in setting BIZ_STORE_MAKATI_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_QC_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_QC_HUB']
        }
        print(payload)
        response = requests.post(url=url, json=payload)
        print(response.text)
    except Exception as e:
        time.sleep(5)
        response = requests.post(url=url, json=payload)
        print("Error in setting BIZ_STORE_QC_HUB ")
        print(str(e))

    try:
        payload = {
            "inventory_item_id": biz_store_inventory_item_id,
            "location_id": config.BIZ_LOCATIONS_LIST['BIZ_STORE_ALABANG_HUB'],
            "available": serialized_product_item_levels['MAIN_STORE_ALABANG_HUB']
        }
        print(payload)
        response = requests.post(url=url, json=payload)
        print(response.text)
    except Exception as e:
        time.sleep(5)
        response = requests.post(url=url, json=payload)
        print("Error in setting BIZ_STORE_ALABANG_HUB ")
        print(str(e))

    return "Finished setting up inventory item levels"


def main_store_set_item_level(main_store_inventory_item_id, serialized_product_item_levels):
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


def main_store_adjust_item_level(
        main_store_inventory_item_id,
        location_id,
        adjustment):
    modifier = -adjustment
    print("Biz Store location id : {}".format(location_id))
    location = serializer.get_main_location_from_biz_location_id(int(location_id))
    print(location)
    print("Main Store location: {}".format(location))
    url = "{}inventory_levels/adjust.json".format(config.MAIN_STORE_DOMAIN)
    print(url)
    payload = {
        "inventory_item_id": main_store_inventory_item_id,
        "location_id": config.MAIN_LOCATIONS_LIST[location],
        "available_adjustment": modifier
    }
    response = requests.post(url=url, json=payload)
    print(response.text)
    return response
