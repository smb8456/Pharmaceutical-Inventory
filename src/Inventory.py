#Class that manages a collection of items in a pharmaceutical inventory

from Item import Item
class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_ID):
        for x in self.items:
            print(f"Checking ID: {x.get_ID()} against {item_ID}")
            if x.get_ID() == item_ID:
                self.items.remove(x)
                return (f"Removed Item ID: {item_ID}")
            
    """
    Returns the description of an item

    :param item_ID: The ID of the item you need a description for
    """
    def get_item(self, item_ID):
        for x in self.items:
            print(f"Checking ID: {x.get_ID()} against {item_ID}")
            if x.get_ID() == item_ID:
                print('Success')
                return x.get_details()
        return 'Item Not Found!'
    
    """
    Returns a list of the items in the pharmaceutical inventory
    """
    def list_items(self):
        item_names = 'Items In Pharmaceutical Inventory:\n'
        for x in self.items:
            item_names += f"ID: {x.get_ID()} | Name: {x.get_name()} | Quantity: {x.get_quantity()}\n"
            #item_names.append(x.get_name())
        return item_names
    
    """
    Updates the quantity of a item in the inventory

    :param item_ID: The ID of the item to update
    :param quantity: Quantity you want to update the item by
    """
    def update_inventory(self, item_ID, quantity):
        for x in self.items:
            print(f"Checking ID: {x.get_ID()} against {item_ID}")
            if x.get_ID() == item_ID:
                x.update_quantity(quantity)
                return f"Updated quantity of {x.get_name()} to {x.get_quantity()}"
        return 'Item Not Found!'
    
    """
    Checks stock of items in the inventory

    :param threshold: The threshold you want to check against the quantity of the items in the inventory
    """
    def check_stock(self, threshold):
        low_stock_items = []
        
        for x in self.items:
            if x.get_quantity() < threshold:
                low_stock_items.append(x)
            
        if low_stock_items:
            items = 'Items In Low Stock:\n'
            for x in low_stock_items:
                items += f"ID: {x.get_ID()} | Quanity: {x.get_quantity()}\n"
            return low_stock_items
        else:
            return 'All items are in stock.'
        
