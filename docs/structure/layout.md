## Structure of code
1. Item Class (Item.py)
   - Attributes
     - ID: Identifier of the item
     - name: Name of the item
     - quantity: Quantity of the item
     - price: Price of the item
     - expiry_Date: Expiration date of the item
     - type: Type of the item
     - manufacturer: Manufacturer of the item
     - description: Description of the item
   - Methods
      - get_name, get_ID, get_expiry_date, get_quantity, get_manufacturer, get_details: Getter methods
       to retrieve attributes of an item
      - update_quantity: Updates the stock level of the item
3. Inventory Class (Inventory.py)
   - Attributes
      - items: List of item objects
   - Methods
      - add_item: Adds an item object to the list
      - remove_item: Removes an item object to the list
      - get_item: Returns the description of an item
      - list_items: Returns a list of the items in the inventory
      - update_inventory: Updates the quantity of an item in the inventory
      - check_stock: Checks stock of items in the inventory
5. Reports Class (Reports.py)
   - Attributes
      - inventory: Instance of an inventory class
   - Methods
      - low_stock_report: Generates a low stock report
      - manufacturer_report: Generates a manufacturer report
      - expiry_report: Generates a expiraction report
