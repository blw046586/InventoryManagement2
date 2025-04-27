# === inventory/manager.py ===
from collections import defaultdict
from inventory.avl_tree import AVLTree

class InventoryManager:
    def __init__(self):
        self.sku_map = {}  # SKU -> product details
        self.category_map = defaultdict(list)
        self.sorted_inventory = AVLTree()  # Sorted by quantity or price

    def add_product(self, sku, product_info):
        self.sku_map[sku] = product_info
        self.category_map[product_info['category']].append(sku)
        self.sorted_inventory.insert(product_info['quantity'], sku)

    def get_product(self, sku):
        return self.sku_map.get(sku)

    def update_quantity(self, sku, new_quantity):
        if sku in self.sku_map:
            self.sorted_inventory.delete(self.sku_map[sku]['quantity'], sku)
            self.sku_map[sku]['quantity'] = new_quantity
            self.sorted_inventory.insert(new_quantity, sku)
