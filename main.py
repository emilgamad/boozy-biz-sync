""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import views

APP = Flask(__name__)
CORS(APP)
API = Api(APP)


# Get (Domain)
API.add_resource(views.Index, '/')

# Get (API index)
API.add_resource(views.APIIndex, '/api/v1')

# POST Main Store Order Creation
API.add_resource(views.MainStoreOrderCreatedView, '/api/v1/order/main')

# POST Biz Store Order Creation
API.add_resource(views.BizStoreOrderCreatedView, '/api/v1/order/biz')

# POST Process received sync info
API.add_resource(views.SyncOrderView, '/api/v1/sync')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
