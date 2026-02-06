"""
You are tasked with creating a simple calculator program in Python. The program should:
1. Ask the user to input two numbers.
2. Ask the user to choose an operation (addition, subtraction, multiplication, division).
3. Perform the chosen operation on the two numbers.
4. Display the result.
5. If the user attempts to divide by zero, the program should catch this error and display an
appropriate error message without crashing.

"""
while True:
    # Making only number based

    while True:
        num_1 = input("Enter your number 1: ")

        if num_1.isdigit():
            num_1 = float(num_1)
            break
        print("Enter only numbers: ")

    # Making only number based
    while True:
        num_2 = input("Enter your number 2: ")

        if num_2.isdigit():
            num_2 = float(num_2)
            break
        print("Enter only numbers: ")

    "Making Function for Add, Sub, Mul, and Divide"

    # Taking input from the user
    while True:
        print()
        choose_option = input(
            "What you want to do (sub/add/mul/div): ").lower().strip()
        print()

        if not choose_option.isdigit() and ("sub" in choose_option or "add" in choose_option or "mul" in choose_option or "div" in choose_option):
            break
        print("Enter only text! and only (sub/add/mul/div)")

    # Addition Condition
    if 'add' in choose_option:
        add = num_1 + num_2
        print(f"The sum of two numbers is {add}")

    # Subtracting Condition
    if 'sub' in choose_option:
        while True:
            option_sub = input(
                f"{num_1} - {num_2} press '1' and {num_2} - {num_1} press '2': ").strip()
            if "1" in option_sub or "2" in option_sub:
                break
        print("Enter Only '1' and '2")

        if "1" in option_sub:
            sub_1 = num_1 - num_2
            print(f"The answer of {num_1} subtracted from  {num_2} is {sub_1}")
        elif "2" in option_sub:
            sub_2 = num_2 - num_1
            print(f"The answer of {num_2} subtracted from  {num_1} is {sub_2}")

    # Multiply Condition
    if "mul" in choose_option:
        mul = num_1 * num_2
        print(f"The Product of {num_1} and {num_2} is {mul}")

    # Division
    if 'div' in choose_option:
        while True:
            option_div = input(
                f"{num_1} / {num_2} press '1' and {num_2} / {num_1} press '2': ").strip()
            if "1" in option_div or "2" in option_div:
                break
        print("Enter Only '1' and '2")

        if "1" in option_div:
            div_1 = num_1 / num_2
            print(
                f"The answer of {num_1} divide from  {num_2} is {round(div_1, 3)}")
        elif "2" in option_div:
            div_2 = num_2 / num_1
            print(
                f"The answer of {num_2} divide from  {num_1} is {round(div_2, 3)}")

    # Ending The loop
    print()  # Spacing
    while True:
        ending = input("Do you want to continue (yes/no): ").lower().strip()
        if ending == "yes":
            break
        elif ending == "no":
            raise SystemExit
        else:
            print("yes/no")
