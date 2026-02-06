# Bonus Distribution for Employees
"""
A company wants to distribute year-end bonuses to its employees based on their performance
ratings. Each employee has a name and a performance rating (out of 5). The bonus distribution is as
follows:
 If an employee has a rating of 5, they receive a bonus of $1,000.
 If an employee has a rating of 4, they receive a bonus of $750.
 If an employee has a rating of 3, they receive a bonus of $500.
 Employees with a rating of 2 or below receive no bonus.

There are five employees: Alice, Bob, Charlie, David, and Eve. Their ratings are:
 Alice has a rating of 5.
 Bob has a rating of 4.
 Charlie has a rating of 3.
 David has a rating of 2.
 Eve has a rating of 5.

Write a Python program that:
1. Takes each employee's name and rating.
2. Determines the bonus amount based on their rating.
3. Prints a message for each employee that shows their name, rating, and bonus amount.
"""

data = [
    ["Alice", 5],
    ["Bob", 4],
    ["Charlie", 3],
    ["David", 2],
    ["Eve", 5],
]

#Applying loop for printing nums of list
for i in data:
    name = i[0]
    rating = i[1]
    if rating == 5:
        print(f"{name.title()} has a {rating} rating of and gets a bonus of \033[1m\"1000$\"\033[0m")
    elif rating == 4:
        print(f"{name.title()} has a {rating} rating of and gets a bonus of \033[1m\"750$\"\033[0m")
    elif rating == 3:
        print(f"{name.title()} has a {rating} rating of and gets a bonus of \033[1m\"500$\"\033[0m")
    else:
        print(f"{name.title()} has a {rating} rating of and do not get any bonus")



