import math

from graphics import *
from time import sleep

def circle_mover():
    win = GraphWin("ball", 500, 500)
    x_coord = 10
    y_coord = 10
    win.setCoords(0, 0, x_coord, y_coord)
    circle = Circle(Point(5, 5), 1)
    circle.draw(win)
    running = True
    while running:
        circle.move(0.1, 0)
        sleep(0.01)
        center_x = circle.getCenter().getX()
        circle_radius = circle.getRadius()
        if center_x > x_coord + circle_radius:
            circle.move(center_x * -1 - circle_radius, 0)
        key = win.checkKey()
        if key == 'q':
            running = False

# short circuiting

# and or
result = False and math.sqrt(-1)

x = 1 and "hi"
print(x)
x = 1 and ''
print(x)
x = 0 and True
print(x)

# can a point have a truthy value?
