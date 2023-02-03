from graphics import Point, Circle, GraphWin
# import graphics
# import math
from math import sqrt, pow
# graphics
# string, int, float, char
#   primitive data types

# math.sqrt(9)
# math.pow(2, 3)

sqrt(9)
pow(2, 3)

age = 57
name = "lin"
center = Point(100, 300)
my_circle = Circle(center, 150)
win = GraphWin("My Cool Window!", 700, 500)

my_center_x = center.getX()
my_center_y = center.getY()
the_circle_center = my_circle.getCenter()
the_circle_center.getX()
the_circle_center.getY()
print(my_center_x)

# input('just waiting...')
