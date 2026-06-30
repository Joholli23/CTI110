# Joshua Holliday
# June 30, 2026
# p4hw1.py
# Design program that enters grades in a list and calculates the average with loops

"""
1. create a list to hold the grades
2. prompt user to enter how many scores they want to enter 
3. create a loop to collect the number of scores
4. validate each score to ensure it's between 0 and 100
5. calculate the lowest grade, highest grade, sum of grades, and score average
6. determine letter grade based on score average
7. display the results in a formatted manner
"""

# Create the list
module_grades = []

# ask user how many scores
num_scores = int(input("How many scores do you want to enter? "))
print()

# create a loop to collect the number of scores
for count in range(num_scores):

    grade = float(input(f"Enter score #{count + 1}: "))

    # Validation loop
    while grade < 0 or grade > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        grade = float(input(f"Enter score #{count + 1} again: "))

    # Store valid score
    module_grades.append(grade)

# Calculate the results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
score_average = sum_grades / len(module_grades)

# determine letter grade
if score_average >= 90:
    letter_grade = 'A'
else:
    if score_average >= 80:
        letter_grade = 'B'
    else:
        if score_average >= 70:
            letter_grade = 'C'
        else:
            if score_average >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'

# Display the results
width = 20
print("\n--------------Results--------------")
print(f"Lowest Score   : {lowest_grade:.1f}")
print(f"Modified List  : {module_grades}")
print(f"Scores Average : {score_average:.2f}")
print(f"Grade          : {letter_grade}")
print("-----------------------------------")


