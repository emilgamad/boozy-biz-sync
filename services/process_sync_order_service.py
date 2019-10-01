"""Process sync order service"""
import json
import store

class ProcessSyncOrderService():

    def __init__(self, sync_order_data):
        sync_order_bytes = sync_order_data['message']['data']
        sync_orders = json.loads(sync_order_bytes.decode())
        self.items = sync_orders['items']
        self.store = sync_orders['store']


    def run(self):
        for orders in self.items:
            product_title = orders['product_title']
            item_levels = orders['item_levels']
            product = orders['product']

            if self.store == 'Main Sync':
                try:
                    biz_store_variant = store.biz_store_get_product_by_title(
                        product_title)
                except Exception as e:
                    print("Error in getting biz store product")
                    print(str(e))
                    return None

                try:
                    if biz_store_variant is None:
                        store.biz_store_create_product(product)
                except Exception as e:
                    print("Error in creating new product in biz store")
                    print(str(e))
                    return None

                try:
                    store.biz_store_set_item_level(item_levels)
                except Exception as e:
                    print("Error in setting item levels in biz store")
                    print(str(e))
                    return None

                return "Biz Store Synced"
            elif self.store == 'Biz Sync':
                main_store_variant = store.main_store_get_product_by_title(
                    variant_title)
                store.main_store_set_item_level(item_levels)
