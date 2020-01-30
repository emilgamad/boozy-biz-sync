import manager
import serializer
import store
import time

class CreateUpdateProductFromMainToBiz():

    def __init__(self, list_of_handles):
        self.list_of_handles = list_of_handles

    def run(self):
        if self.list_of_handles is None:
            return self.list_of_handles
        # for each handle get product by handle from Main site
        counter = 1
        for handle in self.list_of_handles:
            # print("Getting product", handle)
            # if counter >= 1704:
            print(counter, "/"+str(len(self.list_of_handles)))
            # if handle exists in biz update product
            main_store_product = manager.main_store_get_product_by_handle(handle)
            biz_product = manager.biz_store_get_product_by_handle(handle)
            if len(biz_product) > 0:
                biz_store_product_id = biz_product[0]['id']
                biz_store_inventory_item_id = biz_product[0]['variants'][0]['inventory_item_id']
                serialized_product = {}
                serialized_product["product"] = serializer.biz_store_product_serializer(biz_product[0])
                serialized_product["product"]["id"] = biz_store_product_id
                print(store.biz_store_update_product(serialized_product))
            # if handle does not exists in biz create product
            else:
                serialized_product = {}
                serialized_product["product"] = serializer.biz_store_product_serializer(main_store_product[0])
                biz_product = store.biz_store_create_product(serialized_product)
                print(biz_product)
                biz_store_inventory_item_id = biz_product['product']['variants'][0]['inventory_item_id']
            # updating item_levels
            main_store_inventory_item_id = main_store_product[0]['variants'][0]['inventory_item_id']
            main_store_inventory_levels = manager.main_store_get_item_levels_by_id(main_store_inventory_item_id)
            main_store_serialize_item_level = serializer.main_store_serialize_item_level(main_store_inventory_levels)
            store.biz_store_set_item_level(biz_store_inventory_item_id, main_store_serialize_item_level)
            counter+=1

        print("CreateUpdateProductFromMainToBiz finished")
