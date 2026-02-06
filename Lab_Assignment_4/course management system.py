"course management system"

"Tasks to do"
"""
1. Mr. Thompson needs to update the grades for students in the Data Structures course.
Alice grade should be changed to 90, and Charlie has dropped the course, so his entry
should be removed.
2. A new course, Web Development, has been introduced, and Mr. Thompson wants to
add it to the system. He will initially enroll two students, Grace and Henry, with grades
of 92 and 85, respectively.
3. The registrar also needs to check if a student, Bob, is enrolled in the Algorithms
course. If Bob is not found, he needs to add him to the course with a default grade of 80.
4. After reviewing the courses, Mr. Thompson realizes that the Machine Learning course
is not offering grades anymore. He needs to remove this course entirely from the
system.
5. Finally, he wants to retrieve the average grade of students enrolled in the Data
Structures course. If the course does not exist, it should return a default message
indicating that the course is not found.
"""
courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

"Task 1"
title = "TASK 1"
print("*" * 100)
print(title.center(100))

courses["Data Structures"].update({"Alice": 90})
courses["Data Structures"].pop("Charlie")
print("The updated data strcture dictionary is:")
for i in courses["Data Structures"].items():
    print(f"\u25CF {i}")

print()

"Task2"
title = "TASK 2"
print("*" * 100)
print(title.center(100))

courses.update({"Web Development": {"Grace": 92, "Henry": 85}})
print("The updated courses:")
for i in courses.items():
    print(f"\u25CF {i}")

"Task3"
title = "TASK 3"
print("*" * 100)
print(title.center(100))

# applying conditions
if "Bob" in courses["Algorithms"]:
    print("Yes Bob is present in the Algorithm list")
else:
    courses["Algorithms"].update({"Bob": 80})
    print("The Bob was not in the dict. He is added with default value of 80")
    for i in courses["Algorithms"].items():
        print(f"\u25CF {i}")

"Task4"
title = "TASK 4"
print("*" * 100)
print(title.center(100))

print("Removing the Machine Learning course")
courses.pop("Machine Learning")

print("The updated courses:")
for i in courses.items():
    print(f"\u25CF {i}")


"Task5"
title = "TASK 5"
print("*" * 100)
print(title.center(100))
# Checking the data strcture is present or not
course_name = "Data Structures"

if course_name in courses:
    print(f"Yes the subject {course_name} is present in the dict")
    grades = courses[course_name].values()
    total = sum(grades)
    values = len(grades)

    if values == 0:
        print("There is no value inside the dict")
    else:
        avg = total / values
        print(f"The avg value of {course_name} is {avg:.2f}")

else:
    print(f"The \"{course_name}\" is not found")


