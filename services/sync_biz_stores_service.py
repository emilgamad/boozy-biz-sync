"""Syncs inventory item levels in main and biz store every sale"""


class SyncBizStoreService():
    """Sync Store Service"""

    def __init__(self, sync_details):
        self.sync_details = sync_details

    def run(self):
        for variant in self.sync_details:

            variant_title = self.sync_details['title']

            # variant_id = manager.biz_store_get_variant_id_by_title()


        # Serialize product
        # Create (POST) product in biz_store
        # Log creation
