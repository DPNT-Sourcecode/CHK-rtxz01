# noinspection PyUnusedLocal
# skus = unicode string
"""
 As mentioned below, constants should be in seperate file, but to make it easier to
 Review I've left it here
"""
KNOWN_SKUS = ["A", "B", "C", "D"]

def checkout(skus):
    # Verify all items in sku string are valid strings and known
    # Check if input string is a string
    if not isinstance(skus, str):
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
        basket.scan(sku.upper())

    total = basket.checkout()
    return total

class Item():
    # Init function to set default values for child objects
    def __init__(self):
        self.total_cost = 0
        self.single_cost = 0
        self.quantity = 0
        self.discount_quantity = 0
        self.discount_amount = 0

    # Cost function rings up the value of the quantity and cost of each item
    def cost(self):
        self.total_cost = self.single_cost * self.quantity
        self.discount()

    # Discount function calculates how many applicable discounts are available and reduces cost
    def discount(self):
        # Prevent // 0 error
        if self.discount_quantity == 0:
            return
        valid_discounts = self.quantity // self.discount_quantity
        self.total_cost = self.total_cost - self.discount_amount * valid_discounts

    # Scan adds another quantity of an item to the basket
    def scan(self):
        self.quantity += 1

"""
Below are definitions for individual items, their costing and their discounts. 
"""
class SKU_A(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 50
        self.discount_quantity = 3
        self.discount_amount = 20

class SKU_B(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 30
        self.discount_quantity = 2
        self.discount_amount = 15

class SKU_C(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 20

class SKU_D(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 15

"""
 Ideally this and other constants would be in another file but for simplicity of review I'll
 leave it like this. KNOWN_SKUS wouldn't need to exist since  SKU_ITEM_MAP.keys() would work.
"""
SKU_ITEM_MAP = {"A": SKU_A, "B": SKU_B, "C": SKU_C, "D": SKU_D}


class Basket():
    # Init holds the baskets contents as singleton objects with quantity, value and cost values
    def __init__(self):
        self.items = {}

    # Method for adding new item to basket
    # - param sku = letter code of item SKU that has been scanned
    def scan(self, sku):
        if sku in self.items.keys():
            self.items[sku].scan()
        else:
            self.items[sku] = SKU_ITEM_MAP[sku]()
            self.items[sku].scan()

    # Calculates total cost of items in basket
    def checkout(self):
        total_cost = 0
        for item in self.items.values():
            item.cost()
            total_cost += item.total_cost

        return total_cost





