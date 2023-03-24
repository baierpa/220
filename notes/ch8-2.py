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

def truthy_falsy():
    x = True and False
    print(x)
    # T and T
    x = 1 and "hi"
    print(x)
    # T and F
    x = "hey!" and []
    print(x)
    # F and T
    x = 0 and [1,2,3,4]
    print(x)
    # F and F
    x = "" and 0
    print(x)

    # T or T
    x = "hi" or 9
    print(x)
    # T or F
    x = [1,2,3,4,5] or ""
    print(x)
    # F or T
    x = False or 87
    print(x)
    # F or F
    x = 0 or False
    print(x)

def transfer():
    answer = input('do you want to transfer all of you money to us (yes or no)? ')
    first_letter = answer[0]
    if first_letter == 'Y' or first_letter == 'y':
        print('thank you! transferring...')
    else:
        print('ok. see ya.')

ans = input('what is your favorite icecream (default is vanilla)? ')
ans = ans or 'vanilla'
print("oh, i like", ans, 'too!')