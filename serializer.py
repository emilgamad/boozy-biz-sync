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
        product_id = item['product_id']
        try:
            product = manager.main_store_get_product_by_id(product_id)
        except Exception as e:
            print("Error in getting product {}".format(product_id))
            print(str(e))
            return None
        sync_details[product['title']] = {
            "product": product}
    order = {}
    order['store'] = "Sync to Biz"
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
        product_id = item['product_id']
        try:
            product = manager.biz_store_get_product_by_id(product_id)
        except Exception as e:
            print("Error in getting product {}".format(product_id))
            print(str(e))
            return None
        sync_details[product['title']] = {
            "product": product}
    order = {}
    order['store'] = "Sync to Main"
    order['items'] = sync_details
    return json.dumps(order)


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
