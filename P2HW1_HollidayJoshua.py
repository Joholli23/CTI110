# Joshua Holliday
# June 17, 2026
# p2hw1.py
# Edit and enhance existing programs

print("This program calculates and displays travel expenses")
print()

trip_budget = int(input("Enter budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas_cost = int(input("How much do you think you will spend on gas?: "))
print()

hotel_cost = int(input("Approximately, how much will you need for accomodation/hotel?: "))
print()

food_cost = int(input("Lastly, how much do you need for food?: "))
print()

print("------------Travel Expenses------------")
width = 20

print(f"{'Location:':{width}}{destination:<{width}}")
print(f"{'Initial Budget:':{width}}{f'${trip_budget:.2f}':<{width}}")
print(f"{'Fuel:':{width}}{f'${gas_cost:.2f}':<{width}}")
print(f"{'Accommodation:':{width}}{f'${hotel_cost:.2f}':<{width}}")
print(f"{'Food:':{width}}{f'${food_cost:.2f}':<{width}}")
print("---------------------------------------")
print()
remaining_balance = trip_budget - (gas_cost + hotel_cost + food_cost)
print(f"{'Remaining Balance:':{width}}{f'${remaining_balance:.2f}':<{width}}")