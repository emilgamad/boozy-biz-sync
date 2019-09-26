"""Library of functions that the api runs for each particular call"""
from flask import request, jsonify, Response
from flask_restful import Resource, reqparse
from flask_restful.utils import cors
from services.sync_biz_stores_service import SyncBizStoreService
import serializer

parser = reqparse.RequestParser()

class Index(Resource):
    """Index View"""

    @cors.crossdomain(origin='*')
    def get(self):
        return "Boozy Biz Sync API"


class MainStoreOrderCreatedView(Resource):
    """Main Store Order Created View"""

    @cors.crossdomain(origin='*')
    def post(self):
        order_data = request.get_json()
        serialized_order = serializer.main_sync_order_serializer(order_data)
        if serialized_order is None:
            return Response(status=200)
        # SyncBizStoreService(serialized_order).run()
        return serialized_order
