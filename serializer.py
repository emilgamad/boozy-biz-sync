"""Serializes received data"""
import config
import json

def serialize_item_level(item_levels):
    serialized_item_levels = {}
    for item_level in item_levels:
        for location in config.locations_list:
            if config.locations_list[location] == item_level['location_id']:
                serialized_item_levels[location] = item_level['available']
    return serialized_item_levels


def main_sync_order_serializer(order_data):
    """Serializes order data"""
    import manager
    sync_details = {}
    order = order_data['order']
    print(order)

    variant_id_list = order['line_items']
    for item in variant_id_list:
        variant_title = item['title']
        variant_id = item['variant_id']
        product_id = item['product_id']
        product = manager.main_store_get_product_by_id(product_id)
        # if 'b2b' in product['tags']:
        variant = manager.main_store_get_variant_by_id(variant_id)
        inventory_item_id = variant['inventory_item_id']
        item_levels = manager.main_store_get_item_levels_by_id(inventory_item_id)
        serialized_item_levels = serialize_item_level(item_levels)
        sync_details[variant_title] = {
            "variant_title": variant_title,
            "item_levels": serialized_item_levels,
            "product": product
        }
    return json.dumps(sync_details)



        # Get variant
        # Get inventory item id
        # Get get item levels
        # Check if destination has variant title
            # if no
                # create variant
            # if yes
                # get destination variant id
                # get destination inventory item id
                # update item levels


    return sync_details
