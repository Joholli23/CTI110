# Joshua Holliday
# June 9, 2026
# p1hw1.py
# Calculate and display travel expenses

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
print("Location:", destination)
print("Initial Budget:", trip_budget)
print()
print("Fuel", gas_cost)
print("Accomodation", hotel_cost)
print("Food", food_cost)
print()
remaining_balance = trip_budget - (gas_cost + hotel_cost + food_cost)
print("Remaining Balance:", remaining_balance)