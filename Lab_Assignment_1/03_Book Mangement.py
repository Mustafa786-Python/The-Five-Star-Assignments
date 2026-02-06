# Book Management System
welcome = "Welcome to the Book Mangement System"
print("*" * 100)
print(welcome.center(100))
print("*" * 100)


print()
heading = "Books List"
title = f"""
{" " * 30 + "-" * 40}
{" " * 30 + heading.center(40)}
{" " * 30 + "-" * 40}
"""
print(title)
books = ["Atomic Habits", "Quran Majeed", "Deep Work"]
for i in books:
    print(f"\u25CF {i}")
print()

#For Stoping Loop
stop_program = False

while True:

    # Adding Command
    while True:
        option = input("What you want to do (add/remove/check): ").lower().strip()
        print()
    # Making smart
        if not option.isdigit() and ("add" in option or "remove" in option or "check" in option):
            break
        print("add/remove/check")

    # Taking input from the user
    book_name = input("Enter the book name: ").title()
    print()
    # Maing input perfect
    book_name_split = book_name.split()
    clean_book_name = " ".join(book_name_split)

    if "add" in option:
        # # Adding books
        for i in books:
            if clean_book_name in books:
                print(f"It is there at index {books.index(clean_book_name)}")
                break
            else:
                books.append(clean_book_name)
                break
        print(books)

    elif "check" in option:
        # Checking books:
        if clean_book_name in books:
            print(
                f"Your searched book is in the list at index {books.index(clean_book_name)}")
        else:
            print(f"Your serched book is not on the list")
        print(books)

    else:
        # Removing books
        for i in books:
            if clean_book_name in books:
                remove = books.remove(clean_book_name)
                print(books)
                break
            else:
                print("The remvoing books is not in the list")
    

    # Ending the loop
    while True:
        print()
        end = input("Do you want to continue (yes/no): ").lower().strip()
        print()
        if end == "yes":
            break                  # only breaks the INNER loop
        elif end == "no":
            stop_program = True
            break                  # break inner loop, then we'll break outer
        else:
             
            print("Write only yes/no")
    if stop_program:
        break      


print(f" Final Book List {title}")
for i in books:
    print(f"\u25CF {i}")
print()
