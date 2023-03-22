import math

from graphics import *
from time import sleep


def circle_draw():
    win = GraphWin("ball", 500, 500)
    x_coord = 10
    y_coord = 10
    win.setCoords(0, 0, x_coord, y_coord)
    circle = Circle(Point(5, 5), 1)
    circle.draw(win)

    while True:
        circle.move(0.1, 0)
        sleep(0.01)
        x = circle.getCenter().getX()
        circle_radius = circle.getRadius()
        if x > x_coord + circle_radius:
            circle.move(x * -1 - circle_radius, 0)
        # click = win.checkMouse()
        key = win.checkKey()
        if key == 'q':
            break

# short circuiting
x = 5
x > 7 and math.sqrt(-1)

x = [False]
if x:
    print('ok')