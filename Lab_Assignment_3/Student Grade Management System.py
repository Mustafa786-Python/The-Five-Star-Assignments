"""
You are building a simple Student Grade Management System for a school. The
teacher has recorded the grades of students in a list, but now needs help with several tasks related
to managing these grades.

The list of student grades is as follows:
[85, 90, 78, 92, 88, 76, 95, 89]
The teacher asks you to:
1. Add a new student's grade (80) to the list.
2. Sort the grades in ascending order so that the teacher can review them from lowest to
highest.
3. Find the highest grade in the list.
4. Remove a student's grade (76) from the list because it was mistakenly entered.
5. Count how many students scored above 85.
"""

student_list = [85, 90, 78, 92, 88, 76, 95, 89]

# Add a new student's grade (80) to the list.
student_list.append(80)
print(
    f" the grade 80 is added to the list. The new list is {student_list}", end="\n\n")

# Sort the grades in ascending order so that the teacher can review them from lowest to highest.
print(
    f"The sorted list in the ascending order {sorted(student_list)}", end="\n\n")

# Find the highest grade in the list.
print(f"The highest grade in the list is  {max(student_list)}", end="\n\n")

# Remove a student's grade (76) from the list because it was mistakenly entered.
student_list.remove(76)
print(f"76 is removed from the lsit {student_list}", end="\n\n")

# ...existing code...

# Count how many students scored above 85
count_above_85 = sum(1 for grade in student_list if grade > 85) 

print(f"The number of students who scored above 85 is {count_above_85}", end="\n\n")


