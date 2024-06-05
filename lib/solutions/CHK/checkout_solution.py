# noinspection PyUnusedLocal
# skus = unicode string
"""
 As mentioned below, constants should be in separate file, but to make it easier to
 Review I've left it here
"""
KEY_SINGLECOST = "single_cost"
# Multibuy syntax is [(Quantity needed, discount)]
KEY_MULTIBUY_OFFERS = "multibuy_discount_offers"
# Multiprice syntax is [(Quantity needed of SKU for a free item, SKU)]
KEY_MULTIPRICE_OFFERS = "multiprice_one_free_if"
# BuyXgetYFree syntax is [(Quantity required, amount free)]
KEY_BUYX_GETY_FREE_OFFERS = "buyx_gety_free"
"""
Going to assume any SKU will only be a part of one group discount at a time.
This is what I would assume from a shop, but if this wasn't the case then
there would be a concern about group subests / priorities to worry about which seems
overcomplicated with the current specification
"""
# GroupDiscount key syntax is (Quantity of group needed, total cost for all items, eligible items)
KEY_GROUP_DISCOUNT = "group_discount"
# Known group discounts
GD_3STXYZ_for_45 = (3, 45, "STXYZ")

SKU_DISCOUNT_MAP = {
    "A": {KEY_SINGLECOST: 50, KEY_MULTIBUY_OFFERS: [(3, 20), (5, 50)]},
    "B": {KEY_SINGLECOST: 30, KEY_MULTIBUY_OFFERS: [(2, 15)], KEY_MULTIPRICE_OFFERS: [(2, "E")]},
    "C": {KEY_SINGLECOST: 20,},
    "D": {KEY_SINGLECOST: 15,},
    "E": {KEY_SINGLECOST: 40,},
    "F": {KEY_SINGLECOST: 10, KEY_BUYX_GETY_FREE_OFFERS: [(2, 1)]},
    "G": {KEY_SINGLECOST: 20,},
    "H": {KEY_SINGLECOST: 10, KEY_MULTIBUY_OFFERS: [(5, 5), (10, 20)]},
    "I": {KEY_SINGLECOST: 35,},
    "J": {KEY_SINGLECOST: 60,},
    "K": {KEY_SINGLECOST: 70, KEY_MULTIBUY_OFFERS: [(2, 10)]},
    "L": {KEY_SINGLECOST: 90,},
    "M": {KEY_SINGLECOST: 15, KEY_MULTIPRICE_OFFERS: [(3, "N")]},
    "N": {KEY_SINGLECOST: 40,},
    "O": {KEY_SINGLECOST: 10,},
    "P": {KEY_SINGLECOST: 50, KEY_MULTIBUY_OFFERS: [(5, 50)]},
    "Q": {KEY_SINGLECOST: 30, KEY_MULTIBUY_OFFERS: [(3, 10)], KEY_MULTIPRICE_OFFERS: [(3, "R")]},
    "R": {KEY_SINGLECOST: 50,},
    "S": {KEY_SINGLECOST: 20, KEY_GROUP_DISCOUNT: GD_3STXYZ_for_45},
    "T": {KEY_SINGLECOST: 20, KEY_GROUP_DISCOUNT: GD_3STXYZ_for_45},
    "U": {KEY_SINGLECOST: 40, KEY_BUYX_GETY_FREE_OFFERS: [(3, 1)]},
    "V": {KEY_SINGLECOST: 50, KEY_MULTIBUY_OFFERS: [(2, 10), (3, 20)]},
    "W": {KEY_SINGLECOST: 20,},
    "X": {KEY_SINGLECOST: 17, KEY_GROUP_DISCOUNT: GD_3STXYZ_for_45},
    "Y": {KEY_SINGLECOST: 20, KEY_GROUP_DISCOUNT: GD_3STXYZ_for_45},
    "Z": {KEY_SINGLECOST: 21, KEY_GROUP_DISCOUNT: GD_3STXYZ_for_45},
}

def checkout(skus):
    # Verify all items in sku string are valid strings and known
    # Check if input string is a string
    if not isinstance(skus, str):
        return -1

    # Check all letters inside the string are valid and letters
    for sku in skus:
        if sku not in SKU_DISCOUNT_MAP.keys():
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
    def __init__(self, sku):
        self.sku = sku
        self.total_cost = 0
        self.quantity = 0
        sku_map = SKU_DISCOUNT_MAP[self.sku]
        self.single_cost = sku_map[KEY_SINGLECOST]
        self.multibuy_discount_offers = sku_map.get(KEY_MULTIBUY_OFFERS, [])
        self.multiprice_one_free_if = sku_map.get(KEY_MULTIPRICE_OFFERS, [])
        self.buyx_gety_free = sku_map.get(KEY_BUYX_GETY_FREE_OFFERS, [])
        self.group_discount = sku_map.get(KEY_GROUP_DISCOUNT, None)

    # Cost function rings up the value of the quantity and cost of each item
    def cost(self, all_items):
        self.total_cost = self.single_cost * self.quantity
        self.discount(all_items)

    # Discount function calculates how many applicable discounts are available and reduces cost
    def discount(self, all_items):
        buyX_getY_free_items = self.get_buyx_gety_free_quantity()
        self.quantity -= buyX_getY_free_items
        buyx_gety_free_discount = buyX_getY_free_items * self.single_cost
        best_multiprice_discount = self.get_best_multiprice_discount(all_items)
        best_multibuy_discount = self.get_best_multibuy_discount()
        self.total_cost = (self.total_cost -
                           (best_multibuy_discount + best_multiprice_discount + buyx_gety_free_discount))


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

    # Finds the best applicable discount for buyX get Y free
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
            while quantity_needed < current_quantity:
                free_items += 1
                current_quantity -= 1 + quantity_needed

            if free_items > most_free_items:
                most_free_items = free_items

        return most_free_items

    # @ param - all-items = all items in basket
    # @returns cost for all removed items
    def get_and_apply_group_discount(self, all_items):
        if self.group_discount is None:
            return 0

        quantity_required, total_cost, eligible_items = self.group_discount



    # Scan adds another quantity of an item to the basket
    def scan(self):
        self.quantity += 1

"""
Below are definitions for individual items, their costing and their discounts. 
"""
"""
The previous approach was go in the case that overriding methods would be needed.
But at this point it looks like it's redundant and should be refactored to a map for simplicity
and easier maintenance, if this changes I could always revert to this method.
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
            self.items[sku] = Item(sku)
            self.items[sku].scan()

    # Calculates total cost of items in basket
    def checkout(self):
        total_cost = 0
        for item in self.items.values():
            item.cost(self.items)
            total_cost += item.total_cost

        return total_cost

if __name__ == "__main__":
    checkout("FFF")

