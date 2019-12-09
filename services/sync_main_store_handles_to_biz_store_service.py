import manager
import serializer
import store
import traceback


class SyncMainStoreHandlesToBizStoreService():

    def __init__(self):
        pass

    def run(self):
        biz_product_list = manager.biz_store_get_all_published_products()
        counter = 1
        print(len(biz_product_list))
        for product in biz_product_list:
            if counter >= 1251:
                try:
                    print("Updating", counter)
                    biz_product_handle = product['handle']
                    print(biz_product_handle)
                    biz_inventory_item_item_id = product['variants'][0]['inventory_item_id']
                    print(biz_inventory_item_item_id)
                    main_product = manager.main_store_get_product_by_handle(biz_product_handle)
                    print(main_product)
                    main_inventory_item_item_id = main_product[0]['variants'][0]['inventory_item_id']
                    inventory_levels = manager.main_store_get_item_levels_by_id(main_inventory_item_item_id)
                    serialized_inventory_levels = serializer.main_store_serialize_item_level(inventory_levels)
                    store.biz_store_set_item_level(biz_inventory_item_item_id, serialized_inventory_levels)
                except:
                    print(traceback.format_exc())
                    record = {
                        "counter":counter,
                        "handle": biz_product_handle,
                        "title": product['title'],
                        "biz_product_id": product['id']
                    }
                    print(record)
                    f = open("sync_issues","a+")
                    f.write(str(record)+"\r\n")
                    f.close()

            counter += 1
