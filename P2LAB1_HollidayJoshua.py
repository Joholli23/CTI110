# Joshua Holliday
# June 17, 2026
# p2lab1.py
# The program will calculate the diameter, circumference, and area of a circle

#Import math module to use the constant, math.pi
import math

#Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

#Display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}")
print()

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal points
print(f"The circumference of the circle is {circumference:.2f}")
print()

#Calculate the area
area = math.pi * radius**2

#Display area with 3 decimal points
print(f"The area of the circle is {area:.3f}")

