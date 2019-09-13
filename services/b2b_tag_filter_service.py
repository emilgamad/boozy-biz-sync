"""Checks if product has B2B tag"""


class B2BTagFilterService():
    """Check if b2b product service"""

    def __init__(self, data):
        self.data = data

    def run(self):
        """returns if true if tags contain b2b"""
        return 'b2b' in self.data['tags']
