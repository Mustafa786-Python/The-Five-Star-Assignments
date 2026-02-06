"""
01_Grocery_Store_Check_up_system
"""
'''
You are tasked with creating a basic grocery store checkout system using Python. The program will:
 Ask the user for their name.
 Allow the user to input the price of three grocery items they are purchasing.
 Calculate and display the total amount.
 If the user enters an invalid value (such as a negative price or non-numeric input), the
system should handle the error and prompt the user to re-enter the correct price.
 Once the total is displayed, the program will ask if the user wants to apply a membership
discount. If yes, the total amount should be recalculated with a 10% discount.
'''
# Welcoming
title = "GROCERY STORE CHECKOUT SYSTEM"

print("=" * 100)
print(title.center(100))
print("=" * 100)

# List making
groceries = []

# Inputs from the user
name = input("Enter your name: ").title().strip()
groceries.append(name)
print()

for i in range(1, 4):
    items = input(f"Enter the {i} grocerry item: ").title().strip()

    # making prise only for positive numbers
    while True:
        prize = input(f"Enter the prize of {i}: ")
        if prize.isdigit():
            prize = float(prize)
            break
        else:
            print()
            print("Enter prize in positive numbers.")
    print()

    # adding the elements in the list
    groceries.append([items, prize])

    # Adding the prize
prize1  = (groceries[1][1]) + (groceries[2][1]) + (groceries[3][1]) 


# Calculation for discount
discount = prize1 * 0.1
discount_value = prize1 - discount

# Cards of the buyer:
title1 = "Grocery list"
title2 = "Items"

card1 = f"""
{"-" * 40}
{title1.center(40)}
{"-" * 40}

Name: {groceries[0]}

{"-" * 20}
{title2.center(20)}
{"-" * 20}

{groceries[1][0]}: Rs {groceries[1][1]}
{groceries[2][0]}: Rs {groceries[2][1]}
{groceries[3][0]}: Rs {groceries[3][1]}

Total prize: {prize1}
Total prize with discount: {discount_value}
"""
#Second Cardr
card2 = f"""
{"-" * 40}
{title1.center(40)}
{"-" * 40}

Name: {groceries[0]}

{"-" * 20}
{title2.center(20)}
{"-" * 20}

{groceries[1][0]}: Rs {groceries[1][1]}
{groceries[2][0]}: Rs {groceries[2][1]}
{groceries[3][0]}: Rs {groceries[3][1]}

Total prize without discount: {prize1}

"""

# Offering Discount
print()
option = input("Do want to apply a membership discount: ").lower().strip()
if option == "yes":
    print()
    print(card1)
else:
    print()
    print(card2)


