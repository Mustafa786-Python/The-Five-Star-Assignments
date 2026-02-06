"Student Attendance Management System"
title = "WELCOME TO THE STUDENT ATTENDENCE MANAGEMENT SYSTEM"
print(" " * 40, "*" * 100)
print(" " * 40, title.center(100))
print(" " * 40, "*" * 100)
print()

stu_list = []

# Applying the loop
while True:
    stu_name = input("Enter the student name: ").strip()

    # skipping empty space
    if stu_name == "":
        continue
    if stu_name.lower() == "done":
        break

    name = stu_name.title()

    # Condition for adding or removing loop
    if name in stu_list:
        print(f"{name} is already in the list")
        print()
    else:
        stu_list.append(name)
        print(f"The {name} is added to the list")
        print()

# Printing the student list
heading = "Student Attendance List"
title = f"""
{" " * 30 + "-" * 40}
{" " * 30 + heading.center(40)}
{" " * 30 + "-" * 40}
"""
print(title)
for i in stu_list:
    print(f"\u25CF {i}")