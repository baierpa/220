from graphics import Point, Circle, GraphWin

# import math
# from math import sqrt, pow
# int, float, string, char
#   primitive data types

# math.sqrt(9)
# sqrt(9)

age = 7
name = "john"
last_name = "smith"
my_point = Point(200, 300)
center = Point(100, 600)
my_circle = Circle(center, 150)
title = "My Cool Window!"
win = GraphWin(title, 700, 500)

the_x_value = my_point.getX()
print(the_x_value)
print(my_circle.getY())

# input('just waiting...')