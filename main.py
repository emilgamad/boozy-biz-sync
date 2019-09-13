""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import store
import views

APP = Flask(__name__)
CORS(APP)
API = Api(APP)

# Get (index)
API.add_resource(views.Index, '/api/v1')

# Main Store Webhooks
API.add_resource(views.MainStoreCreateProductView, '/api/v1/main_store/product/create')
API.add_resource(views.MainStoreUpdateProductView, '/api/v1/main_store/product/update')
API.add_resource(views.MainStoreDeleteProductView, '/api/v1/main_store/product/delete')

# Biz Store Webhooks
API.add_resource(views.BizStoreCreateProduct, '/api/v1/biz_store/product/create')
API.add_resource(views.BizStoreCreateUpdate, '/api/v1/biz_store/product/update')
API.add_resource(views.BizStoreCreateDelete, '/api/v1/biz_store/product/delete')

if __name__ == '__main__':
    store.Store().start_sync_store_listener_service()
    APP.run(host='0.0.0.0', port=8080, debug=True)
