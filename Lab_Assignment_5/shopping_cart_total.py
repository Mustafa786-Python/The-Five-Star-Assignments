"""
You have a list of toys in a shopping cart. Each toy has a name and a price, but the price is stored as a string (like "19.99"). Your goal is to:

Convert the string prices into numbers so you can do math with them.

Calculate the subtotal by adding all the toy prices together.

Apply a discount (like 10%) to the subtotal to get the final total.

Convert the final total back into a string with two decimal places to make it look like money.

Display everything nicely: each toy’s name, its price, the subtotal, and the final total after discount.

In short: convert → calculate → apply discount → format → display.
"""


# Item prices as strings
toy_car_price = "19.99"
puzzle_price = "5.50"
story_book_price = "3.25"

# Covert them into float
toycar_num = float(toy_car_price)
puzzle_num = float(puzzle_price)
story_book_num = float(story_book_price)

# total
sub_total = toycar_num + puzzle_num + story_book_num

discount = 0.10
dis_subtotal = sub_total*(1 - discount)

card = f"""
Toy Car = ${toy_car_price}
Puzzle = ${puzzle_price}
Story Book = ${story_book_price}
Total = ${sub_total}
With Discount = ${dis_subtotal}
"""

print(card)
