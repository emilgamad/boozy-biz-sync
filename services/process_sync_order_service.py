"""Process sync order service"""
import json
import store
import manager
import serializer

class ProcessSyncOrderService():

    def __init__(self, sync_order_data):

        sync_orders = sync_order_data['message']['data']
        # sync_orders = json.loads(sync_order_bytes.decode())
        self.items = sync_orders['items']
        self.store = sync_orders['store']
        print(self.store)

    def run(self):
        for orders in self.items:
            product_title = orders
            product = self.items[product_title]['product']
            product_inventory_item_id = product['variants'][0]['inventory_item_id']

            if self.store == 'Sync to Biz':
                try:
                    biz_store_product = manager.biz_store_get_product_by_title(
                        product_title)
                except Exception as e:
                    print("Error in getting biz store product")
                    print(str(e))
                    return None

                if len(biz_store_product) == 0:
                    continue

                biz_store_inventory_item_id =  biz_store_product['variants'][0]['inventory_item_id']
                print(biz_store_inventory_item_id)
                try:
                    product_item_levels = manager.main_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_product_item_levels = serializer.main_store_serialize_item_level(product_item_levels)
                    biz_item_levels = manager.biz_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_biz_item_levels = serializer.biz_store_serialize_item_level(biz_item_levels)
                except Exception as e:
                    print("Error in getting item levels from main store")
                    print(str(e))
                    return None
                print(serialized_product_item_levels)
                print(serialized_biz_item_levels)
                try:
                    response = store.biz_store_set_item_level(
                        biz_store_inventory_item_id,
                        serialized_product_item_levels)
                    print(response.text)
                except Exception as e:
                    print("Error in getting item levels in biz store")
                    print(str(e))
                    return None
                return "Biz Store Synced"

            elif self.store == 'Sync to Main':
                try:
                    main_store_product = manager.main_store_get_product_by_title(
                        product_title)
                except Exception as e:
                    print("Error in getting main store product")
                    print(str(e))
                    return None

                if len(biz_store_product) == 0:
                    continue

                main_store_inventory_item_id = main_store_product['variants'][0]['inventory_item_id']
                print(main_store_inventory_item_id)
                try:
                    product_item_levels = manager.biz_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_product_item_levels = serializer.biz_store_serialize_item_level(product_item_levels)
                    main_item_levels = manager.main_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_main_item_levels = serializer.main_store_serialize_item_level(main_item_levels)
                except Exception as e:
                    print("Error in getting item levels from main store")
                    print(str(e))
                    return None
                print(serialized_product_item_levels)
                print(serialized_main_item_levels)
                try:
                    response = store.main_store_set_item_level(
                        biz_store_inventory_item_id,
                        serialized_product_item_levels)
                    print(response.text)
                except Exception as e:
                    print("Error in getting item levels in biz store")
                    print(str(e))
                    return None
                return "Main Store Synced"
