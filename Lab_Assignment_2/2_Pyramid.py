# create a pyramid pattern using a for loop in Python
n = int(input("Enter a number rows: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print('*' * ((2 * i) - 1))
