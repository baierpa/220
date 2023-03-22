import math

from graphics import *
from time import sleep

def circle_mover():
    win = GraphWin("ball", 500, 500)
    x_coord = 10
    y_coord = 10
    win.setCoords(0,0,x_coord,y_coord)
    circle = Circle(Point(x_coord * .8, y_coord / 2), 1)
    circle.draw(win)
    playing = True
    while playing:
        circle.move(0.1, 0)
        sleep(0.01)
        x = circle.getCenter().getX()
        circle_radius = circle.getRadius()
        if x > x_coord + circle_radius:
            circle.move(x * -1 - circle_radius, 0)
        # click = win.checkMouse()
        # if click != None:
        #     click_x = click.getX()
        #     if click_x > x_coord * .8:
        #         break
        key = win.checkKey()
        if key == 'q':
            break
x = 5
x > 10 and math.sqrt(-1)
print('hi')

x = [False]
if x:
    print('ok')