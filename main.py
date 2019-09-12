""" Main module to run boozy-biz-sync. Synchronizes sales between main boozy site and boozy biz site when either store makes a sale"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import views

app = Flask(__name__)
CORS(app)
api = Api(app)

# Get (index)
api.add_resource(views.Index, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
