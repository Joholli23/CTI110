# Joshua Holliday
# June 25, 2026
# p3hw2.py
# Salary calculator with overtime

"""
1. request employee name, hours worked, and pay rate
2. evaluate if employee worked overtime and calculate gross pay
    2.1. take any hour after 40 and multiply by 1.5 times the pay rate for overtime pay
    2.2. calculate regular pay for the first 40 hours
    2.3. the else statement will calculate regular pay and zero out overtime pay if the employee worked 40 hours or less
3. display results in a formatted manner adding a header and separating the results with a line
    3.1. display any pay calculations with a dollar sign and two decimal places
"""

# request employee info
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# evaluate overtime
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# display results for this employee
print("----------------------------------------------------------")
print(f"Employee Name: {name}")
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Hours":<15}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
print("------------------------------------------------------------------------------------------")
print(f"{hours:<15}{rate:<12}{overtime_hours:<15}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")