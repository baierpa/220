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


def truthy_falsy():
    x = [False]
    if x:
        print('ok')

    x = 3 > 7 or False
    print(x)

    # T and T
    x = 7 and "hello"
    print(x)
    # T and F
    x = "hey" and []
    print(x)
    # F and T
    x = 0 and [1, 2, 3, 4, 5]
    print(x)
    # F and F
    x = [] and ''
    print(x)

    # T or T
    x = 99 or ['hello', 'world!']
    print(x)
    # T or F
    x = True or ''
    print(x)
    # F or T
    x = '' or [1, 2, 3]
    print(x)
    # F or F
    x = '' or 0
    print(x)


def transfer():
    answer = input('do you want to transfer all of your money to us (yes/no)? ')
    first_letter = answer[0]
    if first_letter == 'Y' or first_letter == 'y':
        print('great, thanks! transferring...')
    else:
        print('whatever. see ya')


def ice_cream():
    order = input("what ice cream do you want [default is vanilla]? ")
    final_order = order or 'vanilla'
    print('one', final_order, 'ice cream comin up!')
