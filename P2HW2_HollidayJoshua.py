# Joshua Holliday
# June 17, 2026
# p2hw2.py
# Design program that enters grades in a list and calculates the average

# Create the list
module_grades = []

# Enter grades for each module; append will add the grade to the list
grade1 = float(input("Enter grade for Module 1: "))
module_grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
module_grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
module_grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
module_grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: "))
module_grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
module_grades.append(grade6)

# Calculate the results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
average_grade = sum_grades / len(module_grades)

# Display the results
width = 20
print("------------Results------------")
print(f"{'Lowest grade:':{width}}{f'{lowest_grade:.1f}':<{width}}")
print(f"{'Highest grade:':{width}}{f'{highest_grade:.1f}':<{width}}")
print(f"{'Sum of grades:':{width}}{f'{sum_grades:.1f}':<{width}}")
print(f"{'Average grade:':{width}}{f'{average_grade:.2f}':<{width}}")
print("-------------------------------")


