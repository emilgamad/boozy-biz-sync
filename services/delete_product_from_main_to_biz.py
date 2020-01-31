import manager
import store


class DeleteProductFromMainToBiz():
    def __init__(self, main_store_product_id):
        self.main_store_product_id = main_store_product_id

    def run(self):
        main_store_product = manager.main_store_get_product_by_id(self.main_store_product_id)
        main_store_handle = main_store_product.get("handle", None)
        if main_store_handle is not None:
            biz_store_product = manager.biz_store_get_product_by_handle(main_store_handle)
            biz_store_product_id = biz_store_product['product']['id']
            response = store.biz_store_delete_item(biz_store_product_id)
            print(response)
