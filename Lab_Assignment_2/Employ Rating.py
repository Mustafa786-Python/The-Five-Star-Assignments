
data = []

while True:
    name = input("Enter employ name: ").title().strip()
    print()

    # Read and validate rating
    while True:
        rating = input("Enter a rating (1/5): ")
        print()
        if rating.isdigit():
            rating = int(rating)
            if rating >= 1 and rating <= 5:
                break
        print("Invalid rating. Please add a number b/w 1 and 5.", end="\n\n")

    # appeding in the list if it is b/w 1 and 5
    if rating == 1 or rating == 2 or rating == 3 or rating == 4 or rating == 5:
        data.append([name, rating])
    else:
        print("Sorry! We could not add it. Enter a ranting between 1 and 5")

    # Ask for continue
    option = input("Do you want to coninue: ").lower().strip()
    print()
    if option == 'no':
        break
print()
print(data)
