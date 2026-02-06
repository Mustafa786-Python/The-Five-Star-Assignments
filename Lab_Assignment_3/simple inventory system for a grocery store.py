"Simple inventory system for a grocery store"
grocery_list = ("Apples", "Bananas", "Oranges", "Grapes", "Bananas", "Oranges", "Grapes", "Bananas"
                ,"Oranges", "Grapes", "Bananas","Oranges", "Grapes", "Bananas","Oranges", "Grapes", "Bananas")

# finding the index of the banana
print(f"The index of banana is {grocery_list.index("Bananas")}")

# Counting how many times the bananas are in the list
print(f"The banana has repeated {grocery_list.count("Bananas")} times")
