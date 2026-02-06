import copy
"Tasks to do"
"""
1. Create a backup copy of the books dictionary, so she has an original record even if she
makes changes to the main dictionary.
2. Print all book titles and their prices to check the current inventory.
3. Calculate the total value of all the books by summing up the prices.
4. A customer just bought 1984 Remove this book from the main inventory and display a
message showing the book title and price that was sold.
"""
books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice&quot": 9.99,
    "Moby Dick&quot": 8.99
}

# Task1
books_copy = copy.deepcopy(books)

# Task2
for keys, values in books_copy.items():
    print(f"{keys} = {values}")
print()

# Task 3
print("--" * 50)
print()
print("Sum of all prices")
add = sum(books_copy.values())
print(f"The totol amount of money of all books {add}")


# Task 4
print("--" * 50)
print()
print("Removing \"1984\"")
removed = books_copy.pop("1984")
print(books_copy)
