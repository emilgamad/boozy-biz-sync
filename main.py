""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import views

APP = Flask(__name__)
CORS(APP)
API = Api(APP)

# Get (index)
API.add_resource(views.Index, '/api/v1')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
