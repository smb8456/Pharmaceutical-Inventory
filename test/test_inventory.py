import unittest
from Inventory import Inventory
from Item import Item

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.amoxicillin = Item("00001", "Amoxicillin 500mg", 15, 15.99, '2024-10-20', 'Capsule', 'AM Pharmaceuticals', 'Treats bacterial infections')
        self.inventory.add_item(self.amoxicillin)

    def test_add_item(self):
        self.assertIn(self.amoxicillin, self.inventory.items)

    def test_remove_item(self):
        self.inventory.remove_item("00001")
        self.assertNotIn(self.amoxicillin, self.inventory.items)

    """def test_check_stock(self):
        low_stock_items = self.inventory.check_stock(10)
        self.assertIn(self.amoxicillin, low_stock_items)"""

if __name__ == '__main__':
    unittest.main()