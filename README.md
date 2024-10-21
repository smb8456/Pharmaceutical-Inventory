# Pharmaceutical-Inventory
Pharmaceutical Inventory Management System Created in Python using as a project 
for my CMPSC 132-002: Programming and Computation II: Data Structures course.

## HOW TO ACCESS
1. Go to: [GitHub repository](https://github.com/smb8456/Pharmaceutical-Inventory).
2. Click on the green "Code" button.
3. Select "Download ZIP" from the dropdown menu.
4. Extract the ZIP file to your desired location on your computer.
5. Open the project folder to access the files.
6. Run the Python scripts directly using your Python environment.

## USAGE & INSTRUCTIONS

## Creating a Items Class
```python
amoxicillin = Item("00001", 'Amoxicillin 500mg Capsules', 15, 15.99, '2024-10-20', 'Capsule', 'AM Pharmaceuticals', 'Used to treat bacterial infections')
ibuprofen = Item("00002", 'Ibuprofen 200mg Tablets', 5, 9.99, '2026-01-09', 'Tablet', 'IM Pharmaceuticals', 'Used for pain relief')
metformin = Item("00003", 'Metformin 500mg Capsules', 0, 12.30, '2025-03-11', 'Tablet', 'MM Pharmaceuticals', 'Used to manage blood sugar')
```

## Creating a Inventory Class
```python
cvs_pharmacy_inventory = Inventory()
```

Adding items to the inventory:
```python
cvs_pharmacy_inventory.add_item(amoxicillin)
cvs_pharmacy_inventory.add_item(ibuprofen)
cvs_pharmacy_inventory.add_item(metformin)
```

Viewing the current items in the inventory:
```python
print(cvs_pharmacy_inventory.list_items())
```

Getting information about a specific item in the inventory:
```python
print(cvs_pharmacy_inventory.get_item("00003"))
```

Updating the quantity of an item in the inventory:
```python
print(cvs_pharmacy_inventory.update_inventory("00003", 15))
```

Checking the stock of the inventory:
```python
cvs_pharmacy_inventory.check_stock(25)
```

## Creating a Reports Class
```python
inventory_reports = Reports(cvs_pharmacy_inventory)
```

Generating a low stock report:
```python
print(inventory_reports.low_stock_report(10))
```

Generating an expiration report::
```python
print(inventory_reports.expiry_report(30))
```

Generating a low manufacturer report::
```python
print(inventory_reports.manufacturer_report('AM Pharmaceuticals'))
```
