from graphics import Circle, Point, GraphWin

# import math
from math import sqrt, pow
# ints, floats, strings, char
#   Primitive Data Types

# math.sqrt(9)
# sqrt(9)

age = 7
name = "john"
center = Point(2, 9)
my_circle = Circle(center, 70)
title = "My Cool Window"
win = GraphWin(title, 700, 500)

point_x_value = center.getX()
circle_center = my_circle.getCenter()
circle_center.getX()
circle_center.getY()
my_circle.draw(win)

input()

# Instance Variables - Values that are stored within a data type
# Object - variable that holds data