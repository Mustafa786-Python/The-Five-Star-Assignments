"dynamic inventory management system for a grocery store."

grocery_tpl = ()  # creating an empty tuple
grocery_list = list(grocery_tpl)

print("You can only add 5 items to the tuple or remove.")  # note
for i in range(5):  # applying loop for adding multiple items in the tuple
    fruit_name = input("Enter fruit {i}: ").strip().title()
    grocery_list.append(fruit_name)
    grocery_tpl = tuple(grocery_list)

heading = "GROCERY TUPLE"
title = f"""
{" " * 30 + "-" * 40}
{" " * 30 + heading.center(40)}
{" " * 30 + "-" * 40}
"""
print(title, end="\n\n")
for i in grocery_tpl:
    print(f"\u25CF {i}")
print()

# COnverting tpl to list
grocery_list = list(grocery_tpl)

value = False  # Loop stoping statement

while True:

    while True:  # Making option to yes or no
        option = input(
            "do you want to remove element from the grocery list (yes/no): ").strip().lower()
        print()
        if "yes" in option:
            break
        elif "no" in option:
            value = True
            break
        print("Only enter (yes/no)")

    # Closing the loop
    if value:
        break

    re = input("name of the item to remove: ").strip().title()
    if re in grocery_list:
        grocery_list.remove(re)
        grocery_tpl = tuple(grocery_list)
        print(f"The {re} has been removed.")
        print(grocery_tpl)
        print()
    else:
        print("The item is not in the list")
        print()


print("Final tuple", title, end="\n\n")
for i in grocery_tpl:
    print(f"\u25CF {i}")
print()
