"""Serializes received data"""
import config
import json
import manager
import traceback

def main_to_biz_inventory_level_serializer(inventory_levels):
    serialized_inventory_levels = []
    for inv in inventory_levels:
        serialized_inventory_levels.append(
            {"location_id": inv['location_id'], "quantity": inv['available']})
    return serialized_inventory_levels

def biz_store_refund_serializer(refund_data):
    print(refund_data)
    sync_order = {}
    order_items = []
    biz_order_id = refund_data['order_id']
    try:
        order =  manager.biz_store_get_order_by_id(biz_order_id)
    except Exception as e:
        print(traceback.format_exc())
        return None
    location = order['note_attributes']
    location_id = refund_data['refund_line_items'][0]['location_id']
    print("biz_store_refund_serializer {}".format(location_id))
    items = refund_data['refund_line_items']
    for item in items:
        product = manager.main_store_get_product_by_id(item['line_item']['product_id'])
        order_items.append({
           "product": product['handle'],
           "quantity": -(item['line_item']['quantity']),
           "location_id": location_id})
    sync_order['items'] = order_items
    sync_order['store'] = "Sync to Main"
    return json.dumps(sync_order)


def main_store_refund_serializer(refund_data):
    print(refund_data)
    sync_order = {}
    order_items = []
    items = refund_data['refund_line_items']
    for item in items:
        print(item)
        product = manager.main_store_get_product_by_id(item['line_item']['product_id'])
        title = product['handle']
        order_items.append({'product': title})
    sync_order['items'] = order_items
    sync_order['store'] = "Sync to Biz"
    return json.dumps(sync_order)


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
    sync_order = {}
    order_items = []
    try:
        order = order_data['order']
    except KeyError:
        order = order_data

    variant_id_list = order['line_items']
    for item in variant_id_list:
        sync_details = {}
        product_id = item['product_id']
        try:
            product = manager.main_store_get_product_by_id(product_id)
        except Exception as e:
            print("Error in getting product {}".format(product_id))
            print(str(e))
            return None
        order_items.append({"product": product['handle']})
    sync_order['items'] = order_items
    sync_order['store'] = "Sync to Biz"
    return json.dumps(sync_order)


def biz_sync_order_serializer(order_data):
    """Serializes order data"""
    sync_order = {}
    order_items = []
    try:
        order = order_data['order']
    except KeyError:
        order = order_data
    variant_id_list = order['line_items']
    # Default QC Hub
    order_location_id = config.BIZ_STORE_QC_HUB
    #
    note_location = order_data['note'].lower()
    if note_location == "makati":
        order_location_id = config.BIZ_STORE_MAKATI_HUB
    elif note_location == "quezon city":
        order_location_id = config.BIZ_STORE_QC_HUB
    elif note_location == "alabang":
        order_location_id = config.BIZ_STORE_ALABANG_HUB
    for item in variant_id_list:
        product = manager.biz_store_get_product_by_id(item['product_id'])
        title = product['handle']
        adjustment = item['quantity']
        location_id = order_location_id
        try:
            for elem in item['note_attributes']:
                if elem['name'] == 'location_id':
                    location_id = elem['value']
        except Exception as e:
            print("Order has no note attribute location id")
            print("location_id used in note to location_id {}".format(location_id))
        order_items.append({"product": title,
                            "quantity": adjustment,
                            "location_id": location_id})
    sync_order['items'] = order_items
    sync_order['store'] = "Sync to Main"
    return json.dumps(sync_order)


def remove_all_ids_from_product(product):
    serialized_product = {}
    serialized_product['product'] = {
        "title": product.get('title', ""),
        "body_html" : product.get('body_html', ""),
        "vendor": product.get('vendor', ""),
        "product_type": product.get('product_type', ""),
        "published": False,
        "handle": product.get('handle', ""),
        "tags": "new",
        "variants": [
            {
                "title": product.get("variants", "")[0].get('title', ""),
                "price": product.get("variants", "")[0].get('price', ""),
                "sku": product.get("variants", "")[0].get('sku', ""),
                "position": product.get("variants", "")[0].get('position', ""),
                "inventory_policy": product.get("variants", "")[0].get('inventory_policy', ""),
                "compare_at_price": product.get("variants", "")[0].get('compare_at_price', ""),
                "fulfillment_service": product.get("variants", "")[0].get('fulfillment_service', ""),
                "inventory_management": product.get("variants", "")[0].get('inventory_management', ""),
                "option1": product.get("variants", "")[0].get('option1', ""),
                "taxable": product.get("variants", "")[0].get('taxable', ""),
                "barcode": product.get("variants", "")[0].get('barcode', ""),
                "grams": product.get("variants", "")[0].get('grams', ""),
                "weight": product.get("variants", "")[0].get('weight', ""),
                "weight_unit": product.get("variants", "")[0].get('weight_unit', ""),
                "inventory_quantity": product.get("variants", "")[0].get('inventory_quantity', ""),
                "old_inventory_quantity": product.get("variants", "")[0].get('old_inventory_quantity', ""),
                "requires_shipping": product.get("variants", "")[0].get('requires_shipping', ""),
            }
        ],
        "options": [
            {
                "name": product.get("options", "")[0].get('name', ""),
                "position": product.get("options", "")[0].get('position', ""),
                "values": [product.get("options", "")[0].get('values', "")[0]]
            }
        ],
        "images": [
            {
                "position": product.get("images", "")[0].get('position', ""),
                "width": product.get("images", "")[0].get('width', ""),
                "height": product.get("images", "")[0].get('height', ""),
                "src": product.get("images", "")[0].get('src', "")
            }
        ]
    }
    return serialized_product


def get_main_location_from_biz_location_id(location_id):
    for elem in config.BIZ_LOCATIONS_LIST:
        if config.BIZ_LOCATIONS_LIST[elem] == location_id:
            biz_store_location = elem
    print(biz_store_location)
    if biz_store_location == "BIZ_STORE_MAKATI_HUB":
        return "MAIN_STORE_MAKATI_HUB"
    if biz_store_location == "BIZ_STORE_QC_HUB":
        return "MAIN_STORE_QC_HUB"
    if biz_store_location == "BIZ_STORE_ALABANG_HUB":
        return "MAIN_STORE_ALABANG_HUB"
