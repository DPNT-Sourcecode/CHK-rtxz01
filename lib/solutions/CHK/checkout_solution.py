# noinspection PyUnusedLocal
# skus = unicode string
"""
 As mentioned below, constants should be in seperate file, but to make it easier to
 Review I've left it here
"""
KNOWN_SKUS = ["A", "B", "C", "D", "E", "F"]

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
        self.multibuy_discount_offers = []
        self.multiprice_one_free_if = []
        self.buyx_gety_free = []

    # Cost function rings up the value of the quantity and cost of each item
    def cost(self, all_items):
        self.total_cost = self.single_cost * self.quantity
        self.discount(all_items)

    # Discount function calculates how many applicable discounts are available and reduces cost
    def discount(self, all_items):
        buyX_getY_free_items = self.get_buyx_gety_free_quantity()
        self.quantity -= buyX_getY_free_items
        best_multiprice_discount = self.get_best_multiprice_discount(all_items)
        best_multibuy_discount = self.get_best_multibuy_discount()
        self.total_cost = (self.total_cost - best_multibuy_discount) - best_multiprice_discount

    # @ param - all-items = all items in basket
    # @returns best applicable multiprice discount
    def get_best_multiprice_discount(self, all_items):
        """
        My understanding here based on the wording is that if a purchase is made of 'EEBB',
        one of the B items is free, bu still counts towards the 2 for promo.
        This would result in a price of 2E (80) + 2B (45) - multipriced (30).
        Otherwise this would rqeirue checking if mulipriced discount is cheaper than multibuy.
        This assumption is based on the wording of
         "All the offers are well balanced so that they can be safely combined."
        """
        """
        After deploying and failing a test I learned that 4 EE purchases should remove the cost even the discounted
        price of the 2B for 45, which Iw as unsure about. Now I assume that when an item is marked as 'Free' it no
        longer counts towards promos for that item, unless this still counts for one item for 45 - 30, will see.
        """
        best_multiprice_discount = 0
        # multiprice_one_free_if is a list of any multipriced offers that translates to a free item
        for multiprice in self.multiprice_one_free_if:
            quantity, item = multiprice
            if item in all_items.keys():
                free_items = all_items[item].quantity // quantity
                best_multiprice_discount += self.single_cost * free_items
                self.quantity = self.quantity - free_items
        return best_multiprice_discount


    # @returns best applicable multibuy discount
    def get_best_multibuy_discount(self):
        # Multibuy discount is only for discounts based on buying X amounts of product
        """
        Some further coments to this below block, it is not 100% optimal, there may possibly be cases where
        different combinations of multibuy works out to a better discount than just doing 2 passes.
        I thought this was suitable for the given complexity of the context. A shop wouldn't in my guess
        have super complicated rules of multibuy.
        However, a recursive function could be used essentially permuting the discounts similar to a decision tree
        to find the 100% best outcome, however I thought for this excersize this was overcomplicated.
        """
        best_multibuy_discount = 0
        for multibuy in self.multibuy_discount_offers:
            first_quantity, first_multibuy_discount = multibuy
            first_discount = first_multibuy_discount * (self.quantity // first_quantity)
            remainder_quantity = self.quantity % first_quantity
            best_second_discount = 0

            for second_multibuy in self.multibuy_discount_offers:
                second_quantity, second_mutlybuy_discount = second_multibuy
                second_discount = second_mutlybuy_discount * (remainder_quantity // second_quantity)

                if first_discount + second_discount > best_multibuy_discount:
                    best_multibuy_discount = first_discount + second_discount

        return best_multibuy_discount

    # @returns amount of free items to be removed from quantity
    def get_buyx_gety_free_quantity(self):
        """
        So at the moment I don't see any possible conflicts with the buyXgetY free
        when it comes to the best offer for the customer, but this potentially might change
        and require a rewrite of how these discounts are handled.
        """
        most_free_items = 0
        for offer in self.buyx_gety_free:
            quantity_needed, free_quantity = offer
            current_quantity = self.quantity
            free_items = 0
            while quantity_needed <= current_quantity:
                free_items += 1
                current_quantity -= 1

            if free_items > most_free_items:
                most_free_items = free_items

        return most_free_items


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
        self.multibuy_discount_offers = [(3, 20), (5, 50)]

class SKU_B(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 30
        self.multibuy_discount_offers = [(2, 15)]
        self.multiprice_one_free_if = [(2, "E")]

class SKU_C(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 20

class SKU_D(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 15

class SKU_E(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 40

class SKU_F(Item):
    def __init__(self):
        super().__init__()
        self.single_cost = 10
        self.buyx_gety_free = [(2, 1)]

"""
 Ideally this and other constants would be in another file but for simplicity of review I'll
 leave it like this. KNOWN_SKUS wouldn't need to exist since  SKU_ITEM_MAP.keys() would work.
"""
SKU_ITEM_MAP = {"A": SKU_A, "B": SKU_B, "C": SKU_C, "D": SKU_D, "E": SKU_E, "F": SKU_F}


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
            item.cost(self.items)
            total_cost += item.total_cost

        return total_cost

if __name__ == "__main__":
    checkout("AAAAAEEBAAABB")