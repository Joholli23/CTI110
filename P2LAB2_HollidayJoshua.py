# Joshua Holliday
# June 17, 2026
# p2lab2.py
# The program will create a dictionary where the key and value pairs are as follows

#Dictionaries - key:value pairs
car = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26.0}
mpg = car["Camaro"]

print("Keys:", list(car))
print()

vehicle = input("Enter a vehicle to see its miles per gallon: ")
print()

mpg = car.get(vehicle)
if mpg is not None:
    print(f"The miles per gallon for that vehicle is {mpg:.2f}")
else:
    print("Vehicle not found.")
print()

miles = float(input("How many miles will you drive the: "))
print()

#Calculate the gallons of gas needed to drive the miles
gallons = miles / mpg
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
print()