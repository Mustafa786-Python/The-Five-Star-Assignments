# Asking form user
quantity = int(input("Enter the quantity of the students: "))
data = []

# Creating a data list of the students
for i in range(1, quantity + 1):
    name = input("Enter the student name: ").strip().title()
    print()
    # Score values assigning
    while True:
        score = input("Enter a score (1/100): ")
        if score.isdigit():
            score = float(score)
            if score >= 1 and score <= 100:
                break
        print("Invalid score. Please add a number (1/100)")

    #appending list
    if score >= 1 and score <= 100:
        data.append([name, score])

#printing student list with score
print()
print(f"""
The list of the student with thier score: 
      {data}
""")

#Apply grading system
for i in data:
    score = i[1]
    #applying the if\else\elif
    if  score < 100 and score >= 90:
        print(f"\u25CF Great performance {i[0]}. You have taken {score}. You met all expectations. Your grade is \033[1m\"A\"\033[0m.")
        print()
    elif  score < 90 and score >= 80:
        print(f"\u25CF Strong effort {i[0]}. You have taken {score}. Keep pushing forward. Your grade is \033[1m\"B\"\033[0m.")
        print()
    elif  score < 80 and score >=70:
        print(f"\u25CF Satisfactory progress {i[0]}. You have taken {score}. More practice will help. Your grade is \033[1m\"C\"\033[0m.")
        print()
    elif  score < 70 and score >=60:
        print(f"\u25CF Below average {i[0]}. You have taken {score}. You need more consistent study. Your grade is \033[1m\"D\"\033[0m.")
        print()
    else:
        print(f"\u25CF Unsatisfactory performance {i[0]}. You have taken {score}. Start from the core concepts. Your grade is \033[1m\"F\"\033[0m.”")
        print()
    

