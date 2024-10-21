import unittest
from Item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.amoxicillin = Item("00001", "Amoxicillin 500mg", 15, 15.99, '2024-10-20', 'Capsule', 'AM Pharmaceuticals', 'Treats bacterial infections')

    def test_item_creation(self):
        self.assertEqual(self.amoxicillin.get_name(), "Amoxicillin 500mg")
        self.assertEqual(self.amoxicillin.get_quantity(), 15)
        self.assertEqual(self.amoxicillin.get_expiry_date(), '2024-10-20')

    def test_update_quantity(self):
        self.amoxicillin.update_quantity(10)
        self.assertEqual(self.amoxicillin.get_quantity(), 25)

if __name__ == '__main__':
    unittest.main()
