#Class that generate reports for a pharmaceutical inventory
from datetime import datetime, timedelta
from Inventory import Inventory
class Reports:
    def __init__(self, inventory):
        self.inventory = inventory
    
    """
    Generates a low stock report

    :param threshold: The threshold you want to check against the quantity of the items in the inventory
    """
    def low_stock_report(self, threshold):
        if self.inventory.check_stock(threshold) != 'All items are in stock!':
            low_stock_items = []
            low_stock_items = self.inventory.check_stock(threshold)
            report = 'LOW STOCK REPORT:\n'
            for x in low_stock_items:
                report += f"{x.get_details()}\n"
        else:
            report = 'There are currently no low quantity items in the inventory.'
        
        return report
    
    """
    Generates a manufacturer report

    :param manufac: The manufacturer you want to generate a report for
    """
    def manufacturer_report(self, manufac):
        manufac_items = []
        for x in self.inventory.items:
            if x.get_manufacturer() == manufac:
                manufac_items.append(x)
        
        if manufac_items:
            report = 'MANUFACTURER REPORT:\n'
            for x in manufac_items:
                report += f"{x.get_details()}\n"
        else:
            report = "This manufacturer has no items in the inventory."
        
        return report
    
    """
    Generates a expiraction report

    :param days_threshold: The threshold you want to check against the expiraction dates of the items in the inventory
    """
    def expiry_report(self, days_threshold):
        today = datetime.now()
        expiring_items = []

        # Loop through items in the inventory
        for x in self.inventory.items:
            # Ensure that the expiry date method is correct
            expiry_date = datetime.strptime(x.get_expiry_date(), "%Y-%m-%d")  # Use the correct method name

            # Calculate the difference in days
            days_until_expiry = (expiry_date - today).days

            # Debugging print statements
            #print(f"Checking item: {x.get_name()}, Expiry Date: {expiry_date.strftime('%Y-%m-%d')}, Days Until Expiry: {days_until_expiry}")

            # Check if the item is close to expiration
            if days_until_expiry <= days_threshold:
                expiring_items.append(x)

        # Prepare the report
        if expiring_items:
            report = 'EXPIRING ITEMS REPORT:\n'
            for x in expiring_items:
                report += f"{x.get_details()}\n"
        else:
            report = "There are no items are close to expiration in the inventory."
        
        return report