"""
A small store wants to keep track of its inventory by allowing a user to add items until they choose
to stop. The user will be prompted to enter the name and quantity of each item in the inventory. The
program will continue to accept items until the user indicates they are finished.
Once the user decides to stop entering items, the program should display the total inventory list,
including each item and its quantity.
"""

print(f"\033[1mWelcome to Inventory Manager\033[0m", end="\n\n")

inventory = []
while True:
    items = input("Enter the name of the item: ").title().strip()
    # Making quantity conditions
    while True:
        quantity = input("Enter the the qantity of the item: ").title().strip()
        if quantity.isdigit():
            score = int(quantity)
            break
        print()
        print("Invalid!. Only numbers can be accepted")
    # Appending the inventory in the list
    inventory.append([items, quantity])

    # Giving option to the user to continue
    while True:
        print()
        option = input("Do you want to continue (yes/no): ").lower().strip()
        print()
        if option == "yes" or option == "no":
            break

        else:
            print()
            print("Only Enter Yes or No")

    if option == "no":
        break

print()
print(f"The total inventory list is {inventory}")
print()
# Printing the inventory list
print(f"\033[1mAll of the stock\033[0m")
for i in inventory:
    items2 = i[0]
    quantity2 = i[1]
    print(f"\u25CF There are {quantity2} {items2}s in the store")
