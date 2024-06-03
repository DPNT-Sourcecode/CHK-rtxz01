

# noinspection PyUnusedLocal
# skus = unicode string

KNOWN_SKUS = ["A", "B", "C", "D"]

def checkout(skus):
    raise NotImplementedError()

class Basket():
    def __init__(self):
        self.items = []

    # Method for adding new item to basket
    # - param sku = letter code of item SKU that has been scanned
    def scan(self, sku):
        if sku.upper not in

class Item():
    def cost(self):
        raise NotImplementedError()

    def discount(self):
        raise NotImplementedError()