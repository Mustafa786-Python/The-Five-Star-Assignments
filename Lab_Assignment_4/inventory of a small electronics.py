# inventory of a small electronics
"""
Liam needs to perform the following tasks to manage his inventory:

1. Update the stock for new shipments of Smartphone (10 additional units) and
Headphones (5 additional units) without changing other items in the inventory.
2. Sell the last item added to the inventory, removing it from the dictionary. Display the
removed item and its quantity.
3. Check the stock level of Camera in the inventory. If the item does not exist, it should
return Out of Stock as the default message.
"""

inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

# Task 1
print("Updating the stocks", end="\n\n")
inventory.update({"Laptop": 20, "Headphones": 35})
for keys, values in inventory.items():
    print(f"{keys} = {values}")

# Task 2
print("--" * 50)
print()
print("Checking the Stocks")
if "Camera" not in inventory.keys():
    print("The camera is out of the Stock")
else:
    print(f'Yes there are {inventory.get("Camera")} cameras')
