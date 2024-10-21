#Class that represents/handles individual items in an pharmecutical inventory
class Item:
    def __init__(self, ID, name, quantity, price, expiry_Date, type, manufacturer, description):
        self.ID = ID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.expiry_Date = expiry_Date
        self.type = type
        self.manufacturer = manufacturer
        self.description = description
    
    def update_quantity(self, x):
        self.quantity += x
    
    def get_name(self):
        return self.name
    
    def get_ID(self):
        return self.ID
    
    def get_expiry_date(self):
        return self.expiry_Date
    
    def get_quantity(self):
        return self.quantity
    
    def get_manufacturer(self):
        return self.manufacturer

    def update_quantity(self, quantity):
        self.quantity += quantity
    
    def get_details(self):
        return (f"\nID: {self.ID}\nName: {self.name}\nQuantity: {self.quantity}\nPrice: {self.price}\nExpiration Date: {self.expiry_Date}\nType: {self.type}\nManufacturer: {self.manufacturer}\nDescription: {self.description}")