import unittest
from Reports import Reports
from Inventory import Inventory
from Item import Item

class TestReports(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.reports = Reports(self.inventory)
        self.amoxicillin = Item("00001", "Amoxicillin 500mg", 5, 15.99, '2024-10-20', 'Capsule', 'AM Pharmaceuticals', 'Treats bacterial infections')
        self.inventory.add_item(self.amoxicillin)

    def test_low_stock_report(self):
        report = self.reports.low_stock_report(10)
        self.assertIn("Amoxicillin 500mg", report)

    def test_expiry_report(self):
        report = self.reports.expiry_report(30)
        self.assertIn("Amoxicillin 500mg", report)

if __name__ == '__main__':
    unittest.main()