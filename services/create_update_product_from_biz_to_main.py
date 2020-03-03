import manager
import serializer
import store
import time

class CreateUpdateProductFromBizToMain():

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
            if len(main_store_product) > 0:
                # updating item_levels
                main_store_inventory_item_id = main_store_product[0]['variants'][0]['inventory_item_id']
                biz_store_inventory_item_id = biz_product[0]['variants'][0]['inventory_item_id']
                biz_store_inventory_levels = manager.biz_store_get_item_levels_by_id(biz_store_inventory_item_id)
                biz_store_serialize_item_level = serializer.biz_store_serialize_item_level(biz_store_inventory_levels)
                print(biz_store_serialize_item_level)
                store.main_store_set_item_level(main_store_inventory_item_id, biz_store_serialize_item_level)
                counter+=1

        print("CreateUpdateProductFromBizToMain finished")
