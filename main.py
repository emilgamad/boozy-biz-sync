""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import store
import views
from services.google_subscription_service import GoogleSubscriptionService

APP = Flask(__name__)
CORS(APP)
API = Api(APP)

# Get (index)
API.add_resource(views.Index, '/api/v1')

# POST Main Store Order Creation
# API.add_resource(views.BizStoreOrderCreatedView, '/api/v1/order/biz')

# POST Main Store Order Creation
API.add_resource(views.MainStoreOrderCreatedView, '/api/v1/order/main')

if __name__ == '__main__':
    GoogleSubscriptionService().run()
    APP.run(host='0.0.0.0', port=8080, debug=True)
