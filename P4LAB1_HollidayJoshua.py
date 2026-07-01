# Joshua Holliday
# July 1, 2026
# p4lab1.py
# Write a turtle graphics program that draws a triangle and a square using loops

# import the library
import turtle

# create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# set turtle options
pen.pensize (5)
pen.pencolor("red")
pen.shape("turtle")

# code to draw the square
for side in range(4):
    pen.forward(100)
    pen.left(90)

# move to top left of square
pen.penup()
pen.goto(0, 100)
pen.setheading(0)
pen.pendown()

# change the triangle color and fill color
pen.fillcolor("yellow")
pen.pencolor("purple")

# while loop that executes 3 times
sides = 3
pen.begin_fill()

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

pen.end_fill()

# wait for user to close window
win.mainloop()
