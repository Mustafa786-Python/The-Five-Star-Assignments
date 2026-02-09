# Problem
"""
Library Book Codes System - Short Version

- Each book has a unique code, e.g. "FIC10521HAR"
- Book Code format:
    [0:3] -> Category (e.g., FIC = Fiction)
    [3:5] -> Shelf Number (e.g., 10)
    [5:8] -> Book Number on that shelf (e.g., 521)
    [8:11] -> Publisher Code (e.g., HAR = HarperCollins)

- Example list of books:
    book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

Tasks for the program:
1. Extract parts of each Book Code using indexing:
    - Category, Shelf Number, Book Number, Publisher
2. Display details clearly for staff
3. Group books by Category or Publisher if needed

"""

'My Version'

book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

book_dic = {}
# loop for accessing according to the pronlem
for code in book_codes:
    cat = code[0:3]
    shelf_no = code[3:5]
    book_no = code[5:8]
    publisher = code[8:11]

    if cat not in book_dic:
        book_dic[cat] = {}

    if shelf_no not in book_dic[cat]:
        book_dic[cat][shelf_no] = {}

    if book_no not in book_dic[cat][shelf_no]:
        book_dic[cat][shelf_no][book_no] = {}

    if book_no not in book_dic[cat][shelf_no][book_no]:
        book_dic[cat][shelf_no][book_no][publisher] = []

    book_dic[cat][shelf_no][book_no][publisher].append(code)
print(book_dic)
print(cat)

for i, (categories, shelf_nums) in enumerate(book_dic.items(), start=1):

    title = f"CATEGORY {i}"
    print("\n")
    print("--" * 50)
    print(title.center(100))
    print("--" * 50)

    print(f"\nCategory: {categories}")

    for shelf_no, book_nums in shelf_nums.items():
        print(f"\nShelf Number: {shelf_no}")

        for book_num, publishers in book_nums.items():
            print(f"\nBook Number: {book_num}")

            for publisher, codes in publishers.items():
                print(f"\nPublisher: {publisher}")

                for code in codes:
                    print(f"\nBook_code: {code}")


# Gemenie Version 
book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

print(f"{'Category':<10} | {'Shelf':<5} | {'Book #':<7} | {'Publisher'}")
print("-" * 40)

for code in book_codes:
    # Slicing the string based on defined positions
    category = code[0:3]
    shelf = code[3:5]
    book_num = code[5:8]
    publisher = code[8:11]

    print(f"{category:<10} | {shelf:<5} | {book_num:<7} | {publisher}")

#GPT Version

# List of book codes
book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

# Go through each book code in the list
for code in book_codes:
    # Extract parts using indexing
    category = code[0:3]      # First 3 characters
    shelf_number = code[3:5]  # Next 2 characters
    book_number = code[5:8]   # Next 3 characters
    publisher = code[8:11]    # Last 3 characters
    
    # Print the details in a readable format
    print("Book Code:", code)
    print("Category:", category)
    print("Shelf Number:", shelf_number)
    print("Book Number:", book_number)
    print("Publisher:", publisher)
    print("--------------------------")
