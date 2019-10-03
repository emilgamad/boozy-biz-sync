"""Library of functions that the api runs for each particular call"""
from flask import request, jsonify, Response
from flask_restful import Resource, reqparse
from flask_restful.utils import cors
from services.google_publish_message_service import GooglePublishMessageService
from services.process_sync_order_service import ProcessSyncOrderService
import serializer

parser = reqparse.RequestParser()

class Index(Resource):
    """Index View"""

    @cors.crossdomain(origin='*')
    def get(self):
        import os
        title = os.getenv('GOOGLE_PROJECT')
        return "Hello World"

class APIIndex(Resource):
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
        GooglePublishMessageService(serialized_order).run()
        return Response(status=200)
        # return serialized_order


class BizStoreOrderCreatedView(Resource):
    """Biz Store Order Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        order_data = request.get_json()
        serialized_order = serializer.biz_sync_order_serializer(order_data)
        if serialized_order is None:
            return Response(status=200)
        GooglePublishMessageService(serialized_order).run()
        return Response(status=200)
        # return serialized_order

class SyncOrderView(Resource):
    """Process received sync details"""
    @cors.crossdomain(origin='*')
    def post(self):
        sync_order_data = request.get_json()
        process_sync_order_service = ProcessSyncOrderService(sync_order_data).run()
        if process_sync_order_service is None:
            return Response(status=200)
        return Response(status=200)
