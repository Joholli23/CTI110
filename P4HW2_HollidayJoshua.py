# Joshua Holliday
# June 30, 2026
# p4hw2.py
# Salary calculator with overtime with loops

"""
1. request employee name and add sentinel value
2. create accumulator variables for overtime pay, regular pay, gross pay, and employee count
3. create a while loop to request employee info until sentinel value is entered
4. evaluate if employee worked overtime and calculate gross pay
    4.1. take any hour after 40 and multiply by 1.5 times the pay rate for overtime pay
    4.2. calculate regular pay for the first 40 hours
    4.3. the else statement will calculate regular pay and zero out overtime pay if the employee worked 40 hours or less
5. add to the accumulator variables for overtime pay, regular pay, gross pay, and employee count
6. display results in a formatted manner adding a header and separating the results with a line
    6.1. display any pay calculations with a dollar sign and two decimal places
7. display the total number of employees entered, total amount paid for overtime, total amount paid for regular pay, and total amount paid for gross pay with a dollar sign and two decimal places
"""

# request employee info
name = input("Enter employee's name or 'done' to finish: ")

# create accumulator variables for overtime pay, regular pay, gross pay, and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    # add employee count plus 1
    employee_count += 1 # employee_count = employee_count + 1
    # ask for employee info
    hours = float(input("How many hours did " + name + " work this week: "))
    rate = float(input("What is " + name + "'s hourly pay rate: "))
    print()


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

    # add to accumulator variables
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # display results for this employee
    print(f"Employee Name: {name}")
    print()
    print("----------------------------------------------------------")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Hours":<15}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("------------------------------------------------------------------------------------------")
    print(f"{hours:<15}{rate:<12}{overtime_hours:<15}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")
    print()

    name = input("Enter employee's name or 'done' to finish: ")
    print()

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular pay: $", format(regularpay_total, ',.2f'))
print("Total amount paid for gross pay: $", format(grosspay_total, ',.2f'))  