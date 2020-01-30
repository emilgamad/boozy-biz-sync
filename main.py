""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import views

app = Flask(__name__)
CORS(app)
api = Api(app)


# Get (Domain)
api.add_resource(views.Index, '/')

# Get (API index)
api.add_resource(views.APIIndex, '/api/v1')

# POST Main Store Order Creation
api.add_resource(views.MainStoreOrderCreatedView, '/api/v1/order/main')

# POST Biz Store Order Creation
api.add_resource(views.BizStoreOrderCreatedView, '/api/v1/order/biz')

# POST Process received sync info
api.add_resource(views.SyncOrderView, '/api/v1/sync')

# POST Main Store Refund Created
api.add_resource(views.MainStoreRefundCreatedView, '/api/v1/refund/main')

# POST Biz Store Refund Created
api.add_resource(views.BizStoreRefundCreatedView, '/api/v1/refund/biz')

# PUT Sync Main Store Handles to Biz Store
api.add_resource(views.SyncMainStoreHandlesToBizStoreView, '/api/v1/sync/biz/hubs')

# POST Main Store Product Create/Update Webhook
api.add_resource(views.MainStoreProductCreateUpdateView, '/api/v1/sync/product/main')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
