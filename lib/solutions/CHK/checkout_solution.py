

# noinspection PyUnusedLocal
# skus = unicode string

KNOWN_SKUS = ["A", "B", "C", "D"]

def checkout(skus):
    # Verify all items in sku string are valid strings and known
    # Check if input string is a string
    try:
        str(skus)
    except Exception:
            return -1

    # Check all letters inside the string are valid and letters
    for sku in skus:
        if sku not in KNOWN_SKUS:
            return -1
        try:
            str(sku)
        except Exception:
            return -1

    basket = Basket()
    for sku in skus:
        basket.scan(sku)

class Item():
    def __init__(self):
        self.total_cost = 0
        self.single_cost = 0
        self.quantity = 0
        self.discount_quantity = 0
        self.discount_amount = 0

    def cost(self):
        self.total_cost = self.single_cost * self.quantity

    def discount(self):
        

    def scan(self):
        self.quantity += 1

class SKU_A(Item):
    def __init__(self):
        super.__init__()
        self.single_cost = 50
        self.discount_quantity = 3
        self.discount_amount = 20

class SKU_B(Item):
    def __init__(self):
        super.__init__()
        self.single_cost = 30
        self.discount_quantity = 2
        self.discount_amount = 15

class SKU_C(Item):
    def __init__(self):
        super.__init__()
        self.single_cost = 20

class SKU_D(Item):
    def __init__(self):
        super.__init__()
        self.single_cost = 15

# Ideally this and other constants would be in another file but for simplicity of review I'll
# leave it like this. KNOWN_SKUS wouldn't need to exist since  SKU_ITEM_MAP.keys() would work.
SKU_ITEM_MAP = {"A": SKU_A, "B": SKU_B, "C": SKU_C, "D": SKU_D}


class Basket():
    def __init__(self):
        self.items = {}

    # Method for adding new item to basket
    # - param sku = letter code of item SKU that has been scanned
    def scan(self, sku):
        if sku in self.items.keys():
            self.items[sku].scan()
        else:
            self.items[sku] = SKU_ITEM_MAP[sku]()

    def checkout(self):
        pass
