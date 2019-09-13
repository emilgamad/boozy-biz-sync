"""Library of functions that the api runs for each particular call"""
from flask import request, jsonify, Response
from flask_restful import Resource, reqparse
from flask_restful.utils import cors
from services.b2b_tag_filter_service import B2BTagFilterService
from services.main_store_create_product_service import MainStoreCreateProductService

parser = reqparse.RequestParser()

class Index(Resource):
    """Index View"""

    @cors.crossdomain(origin='*')

    def get(self):
        return "Boozy Biz Sync API"


class MainStoreCreateProductView(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')

    def post(self):
        data = request.get_json()
        # Check if product tags has 'b2b'
        if B2BTagFilterService(data).run():
            MainStoreCreateProductService(data).run()
        return Response(status=200)

class MainStoreUpdateProductView(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')
    def post(self):
        return Response(status=200)

class MainStoreDeleteProductView(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')
    def post(self):
        return Response(status=200)

class BizStoreCreateProduct(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')
    def post(self):
        Response(status=200)

class BizStoreCreateUpdate(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')
    def post(self):
        Response(status=200)

class BizStoreCreateDelete(Resource):
    """Main Store Create Product View"""

    @cors.crossdomain(origin='*')
    def post(self):
        return Response(status=200)
