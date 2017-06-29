import turtle
import sys

pen = turtle.Turtle()

#draw a circle
def circle(size, color):
	pen.fillcolor(color)
	pen.begin_fill()
	pen.circle(size)
	pen.end_fill()

# drawing a triangle
def triangle(size, color):
	pen.fillcolor(color)
	pen.begin_fill()
	x = 0
	while x < 3:
		pen.forward(size)
		pen.right(120)
		x += 1
	pen.end_fill()

# drawing a star
def star(size, color):
	pen.fillcolor(color)
	pen.begin_fill()
	x = 0
	while x < 5:
		pen.forward(size)
		pen.right(144)
		x += 1
	pen.end_fill()

# get the user's choice for shape, size and color
shape = raw_input("What shape do you want - circle / triangle / star >>")
size = raw_input("How big do you want it to be. Insert a number. >>")
color = raw_input("What colour huh? >>")
# call the appropriate function with the correct parameters
if shape == "circle":
	circle(int(size), color)
elif shape == "triangle":
	triangle(int(size), color)
elif shape == "star":
	star(int(size), color)

turtle.done()
# 