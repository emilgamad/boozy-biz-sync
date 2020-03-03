import serializer
import traceback


class SerializeSyncOrderService():

    def __init__(self, unserialized_sync_orders):

        print("Received unserialized sync order")

        print(unserialized_sync_orders)

        self.unserialized_sync_orders = unserialized_sync_orders

    def run(self):

        origin = self.unserialized_sync_orders.get("origin", None)

        if origin is None:
            print("Unserialized sync order has no origin ")
            return None

        payload = self.unserialized_sync_orders.get("data", None)

        if origin == "Serialize Sync to Biz":
            try:
                serialized_order = serializer.main_sync_order_serializer(payload)
                return serialized_order
            except Exception as e:
                print(traceback.format_exc())
                return None
            if serialized_order is None:
                return None

        elif origin == "Serialize Sync to Main":
            try:
                serialized_order = serializer.biz_sync_order_serializer(payload)
                return serialized_order
            except Exception as e:
                print(traceback.format_exc())
                return None
            if serialized_order is None:
                return None

        elif origin == "Serialize Refund Sync to Main":
            try:
                serialized_refund = serializer.main_store_refund_serializer(payload)
                return serialized_refund
            except Exception as e:
                print(traceback.format_exc())
                return None
            if serialized_order is None:
                return None

        elif origin == "Serialize Refund Sync to Biz":
            try:
                serialized_order = serializer.biz_store_refund_serializer(payload)
                return serialized_refund
            except Exception as e:
                print(traceback.format_exc())
                return None
            if serialized_order is None:
                return None
