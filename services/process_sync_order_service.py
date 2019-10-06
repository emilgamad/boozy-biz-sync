"""Process sync order service"""
import json
import store
import manager
import serializer
import base64

class ProcessSyncOrderService():

    def __init__(self, sync_order_data):

        sync_orders = sync_order_data#['message']['data']
        # try:
        #     sync_orders = json.loads(base64.b64decode(sync_orders).decode())
        # except:
        #     sync_orders = json.loads(base64.b64decode(sync_orders).decode())
        print(sync_orders)
        self.store = sync_orders['store']
        # print(self.store)
        self.items = sync_orders['items']
        print(self.items)

    def run(self):
        for orders in self.items:
            print(orders)
            type(orders)
            product_title = orders['product']
            if self.store == 'Sync to Biz':
                biz_store_product = manager.biz_store_get_product_by_title(
                        product_title)
                if len(biz_store_product) == 0:
                    continue
                product = manager.main_store_get_product_by_title(product_title)
                product_inventory_item_id = product['variants'][0]['inventory_item_id']
                biz_store_inventory_item_id =  biz_store_product[0]['variants'][0]['inventory_item_id']
                print(biz_store_inventory_item_id)
                try:
                    product_item_levels = manager.main_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_product_item_levels = serializer.main_store_serialize_item_level(product_item_levels)
                    biz_item_levels = manager.biz_store_get_item_levels_by_id(biz_store_inventory_item_id)
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
                print("Biz Store Synced")

            elif self.store == 'Sync to Main':
                adjustment = self.items[product_title]['quantity']
                location_id = self.items[product_title]['location_id']
                try:
                    main_store_product = manager.main_store_get_product_by_title(
                        product_title)
                except Exception as e:
                    print("Error in getting main store product")
                    print(str(e))
                    return None

                if len(main_store_product) == 0:
                    continue

                main_store_inventory_item_id = main_store_product['variants'][0]['inventory_item_id']
                print(main_store_inventory_item_id)
                try:
                    product_item_levels = manager.biz_store_get_item_levels_by_id(product_inventory_item_id)
                    serialized_product_item_levels = serializer.biz_store_serialize_item_level(product_item_levels)
                    main_item_levels = manager.main_store_get_item_levels_by_id(main_store_inventory_item_id)
                    serialized_main_item_levels = serializer.main_store_serialize_item_level(main_item_levels)
                except Exception as e:
                    print("Error in getting item levels from main store")
                    print(str(e))
                    return None
                print(serialized_product_item_levels)
                print(serialized_main_item_levels)
                try:
                    response = store.main_store_adjust_item_level(
                        main_store_inventory_item_id,
                        location_id,
                        adjustment)
                    print(response.text)
                except Exception as e:
                    print("Error in setting item levels in main store")
                    print(str(e))
                    return None
                return "Main Store Synced"
