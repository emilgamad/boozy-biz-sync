"""Library of functions that the api runs for each particular call"""
import traceback
import json
from flask import request, jsonify, Response
from flask_restful import Resource, reqparse
from flask_restful.utils import cors
from services.google_publish_message_service import GooglePublishMessageService
from services.process_sync_order_service import ProcessSyncOrderService
from services.sync_main_store_handles_to_biz_store_service import SyncMainStoreHandlesToBizStoreService
import serializer
import config


parser = reqparse.RequestParser()

class Index(Resource):
    """Index View"""
    @cors.crossdomain(origin='*')
    def get(self):
        return jsonify(
            {
                "Project":"Boozy Biz Sync API",
                "Hello":"World",
                "Config":config.GCP_TOPIC_NAME,
                "Domain":config.MAIN_STORE_DOMAIN
            }
        )


class APIIndex(Resource):
    """Index View"""

    @cors.crossdomain(origin='*')
    def get(self):
        return jsonify({"Project":"Boozy Biz Sync API", "Hello":"World"})


class MainStoreProductCreateUpdateView(Resource):
    """Main Store Order Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        product_data = request.get_json()
        print("Main Store Product Created View")
        tags = product_data.get('tags', None)
        if "biz_product" in tags:
            product_data["store"] = "CreateUpdate to Biz"
            print("Received:", product_data)
            GooglePublishMessageService(json.dumps(product_data)).run()
        return Response(status=200)
        # return serialized_order


class BizStoreProductCreateUpdateView(Resource):
    """Main Store Order Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        product_data = request.get_json()
        print("Biz Store Product Created View")
        tags = product_data.get('tags', None)
        if "biz_product" in tags:
            product_data["store"] = "CreateUpdate to Main"
            print("Received:", product_data)
            GooglePublishMessageService(json.dumps(product_data)).run()
        return Response(status=200)
        # return serialized_order


class SyncOrderView(Resource):
    """Process received sync details"""
    @cors.crossdomain(origin='*')
    def post(self):
        print("Sync Triggered")
        sync_order_data = request.get_json()
        try:
            ProcessSyncOrderService(sync_order_data).run()
        except:
            print(traceback.print_exc())
            return Response(status=200)
        return Response(status=200)


class MainStoreOrderCreatedView(Resource):
    """Main Store Order Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        order_data = request.get_json()
        print("Main Store Order Created View")
        print(order_data)
        try:
            order_data['store'] = "Sync to Biz"
            # serialized_order = serializer.main_sync_order_serializer(order_data)
        except Exception as e:
            print(traceback.format_exc())
            return Response(status=200)
        # if serialized_order is None:
        #     return Response(status=200)
        GooglePublishMessageService(order_data).run()
        return Response(status=200)
        # return serialized_order


class BizStoreOrderCreatedView(Resource):
    """Biz Store Order Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        order_data = request.get_json()
        print("Biz Store Order Created View")
        try:
            order_data['store'] = "Sync to Main"
            serialized_order = serializer.biz_sync_order_serializer(order_data)
        except Exception as e:
            print(traceback.format_exc())
            return Response(status=200)
        # if order_data is None:
        #     return Response(status=200)
        GooglePublishMessageService(order_data).run()
        return Response(status=200)
        # return serialized_order


class MainStoreRefundCreatedView(Resource):
    """Main Store Refund Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        refund_data = request.get_json()
        print("Main Store Refund Created View")
        print(refund_data)
        try:
            refund_data['store'] = "Sync Refund to Biz"
            # serialized_refund = serializer.main_store_refund_serializer(refund_data)
        except Exception as e:
            print(traceback.format_exc())
            return Response(status=200)
        # if serialized_refund is None:
        #     return Response(status=200)
        GooglePublishMessageService(refund_data).run()
        return Response(status=200)


class BizStoreRefundCreatedView(Resource):
    """Biz Store Refund Created View"""
    @cors.crossdomain(origin='*')
    def post(self):
        refund_data = request.get_json()
        print("Biz Store Refund Created View")
        print(refund_data)
        try:
            refund_data['store'] = "Sync Refund to Main"
            # serialized_order = serializer.biz_store_refund_serializer(refund_data)
        except Exception as e:
            print(traceback.format_exc())
            return Response(status=200)
        # if serialized_order is None:
        #     return Response(status=200)
        GooglePublishMessageService(refund_data).run()
        return Response(status=200)


class SyncMainStoreHandlesToBizStoreView(Resource):
    """Sync main store items to biz store items"""
    @cors.crossdomain(origin='*')
    def put(self):
        SyncMainStoreHandlesToBizStoreService().run()
        return Response(status=200)


class DeleteProductCreateUpdateView(Resource):
    """Main Store Order Delete View"""
    @cors.crossdomain(origin='*')
    def post(self):
        product_data = request.get_json()
        print("Main Store Product Created View")
        product_data["store"] = "Delete to Biz"
        print("Received:", product_data)
        GooglePublishMessageService(json.dumps(product_data)).run()
        return Response(status=200)
