"""Serializes received data"""
import config
import json

def main_store_serialize_item_level(item_levels):
    serialized_item_levels = {}
    for item_level in item_levels:
        for location in config.MAIN_LOCATIONS_LIST:
            if config.MAIN_LOCATIONS_LIST[location] == item_level['location_id']:
                serialized_item_levels[location] = item_level['available']
    return serialized_item_levels


def biz_store_serialize_item_level(item_levels):
    serialized_item_levels = {}
    for item_level in item_levels:
        for location in config.BIZ_LOCATIONS_LIST:
            if config.BIZ_LOCATIONS_LIST[location] == item_level['location_id']:
                serialized_item_levels[location] = item_level['available']
    return serialized_item_levels


def main_sync_order_serializer(order_data):
    """Serializes order data"""
    import manager
    sync_details = {}
    try:
        order = order_data['order']
    except KeyError:
        order = order_data

    variant_id_list = order['line_items']
    for item in variant_id_list:
        variant_title = item['title']
        variant_id = item['variant_id']
        product_id = item['product_id']
        try:
            product = manager.main_store_get_product_by_id(product_id)
        except Exception as e:
            print("Error in getting product {}".format(product_id))
            print(str(e))
            return None
        try:
            variant = manager.main_store_get_variant_by_id(variant_id)
        except Exception as e:
            print("Error in getting variant {}".format(variant_id))
            print(str(e))
            return None
        print(variant)
        inventory_item_id = variant['inventory_item_id']
        try:
            item_levels = manager.main_store_get_item_levels_by_id(inventory_item_id)
        except Exception as e:
            print("Error in getting item levels {}".format(inventory_item_id))
            print(str(e))
            return None
        serialized_item_levels = main_store_serialize_item_level(item_levels)
        sync_details[variant_title] = {
            "product_title": product['title'],
            "item_levels": serialized_item_levels,
            "product": product
            }
    order = {}
    order['store'] = "Main Sync"
    order['items'] = sync_details
    return json.dumps(order)

def biz_sync_order_serializer(order_data):
    """Serializes order data"""
    import manager
    sync_details = {}
    try:
        order = order_data['order']
    except KeyError:
        order = order_data

    variant_id_list = order['line_items']
    for item in variant_id_list:
        variant_title = item['title']
        variant_id = item['variant_id']
        product_id = item['product_id']
        try:
            product = manager.biz_store_get_product_by_id(product_id)
        except Exception as e:
            print("Error in getting product {}".format(product_id))
            print(str(e))
            return None
        try:
            variant = manager.biz_store_get_variant_by_id(variant_id)
        except Exception as e:
            print("Error in getting variant {}".format(variant_id))
            print(str(e))
            return None
        print(variant)
        inventory_item_id = variant['inventory_item_id']
        try:
            item_levels = manager.biz_store_get_item_levels_by_id(inventory_item_id)
        except Exception as e:
            print("Error in getting item levels {}".format(inventory_item_id))
            print(str(e))
            return None
        serialized_item_levels = biz_store_serialize_item_level(item_levels)
        sync_details[variant_title] = {
            "variant_title": variant_title,
            "item_levels": serialized_item_levels,
            "product": product
        }
    order = {}
    order['store'] = "Biz Sync"
    order['items'] = sync_details
    return json.dumps(order)
