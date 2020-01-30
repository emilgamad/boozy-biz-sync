"""Process sync order service"""
import json
import store
import manager
import serializer
import base64
import traceback
from services.create_update_product_from_main_to_biz import CreateUpdateProductFromMainToBiz

class ProcessSyncOrderService():

    def __init__(self, sync_order_data):

        sync_orders = sync_order_data['message']['data']
        self.sync_orders = json.loads(base64.b64decode(sync_orders).decode())
        print(self.sync_orders)
        self.store = self.sync_orders['store']
        print(self.store)
        self.items = None
        if self.store != "CreateUpdate to Biz":
            self.items = self.sync_orders.get('items', None)
    def run(self):
        if self.items is None:
            handle = self.sync_orders.get('handle', None)
            if handle is not None:
                CreateUpdateProductFromMainToBiz([handle]).run()
        else:
            for orders in self.items:
                product_title = orders['product']
                if self.store == 'Sync to Biz':
                    biz_store_product = manager.biz_store_get_product_by_title(
                            product_title)
                    if biz_store_product is None:
                        print(product_title, "does not exist")
                        continue
                    product = manager.main_store_get_product_by_title(product_title)
                    product_inventory_item_id = product[0]['variants'][0]['inventory_item_id']
                    biz_store_inventory_item_id =  biz_store_product[0]['variants'][0]['inventory_item_id']
                    try:
                        product_item_levels = manager.main_store_get_item_levels_by_id(product_inventory_item_id)
                        serialized_product_item_levels = serializer.main_store_serialize_item_level(product_item_levels)
                        biz_item_levels = manager.biz_store_get_item_levels_by_id(biz_store_inventory_item_id)
                        # serialized_biz_item_levels = serializer.biz_store_serialize_item_level(biz_item_levels)
                    except Exception:
                        print(traceback.format_exc())
                        print("Error in getting item levels from main store")
                        return None
                    try:
                        response = store.biz_store_set_item_level(
                            biz_store_inventory_item_id,
                            serialized_product_item_levels)
                    except Exception as e:
                        print("Error in getting item levels in biz store")
                        print(str(e))
                        return None
                    print("Biz Store Synced")

                elif self.store == 'Sync to Main':
                    print(orders)
                    print(orders['product'])
                    product_title = orders['product']
                    adjustment = orders['quantity']
                    location_id = orders['location_id']
                    main_store_product = manager.main_store_get_product_by_title(
                        product_title)

                    if len(main_store_product) == 0:
                        continue

                    main_store_inventory_item_id =  main_store_product[0]['variants'][0]['inventory_item_id']

                    response = store.main_store_adjust_item_level(
                            main_store_inventory_item_id,
                            location_id,
                            adjustment)
                    print("Main Store Synced")
