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

def truthy_falsy():

    x = [False]
    if x:
        print('ok')

    x = True and False
    print(x)

    # T and T
    x = 3 and "hello"
    print(x)
    # T and F
    x = "hi" and []
    print(x)
    # F and T
    x = 0 and [1,2,3,4,5]
    print(x)
    # F and F
    x = [] and ''
    print(x)

    # T or T
    x = 7 or 'hey'
    print(x)
    # T or F
    x = [1,2,3] or ''
    print(x)
    # F or T
    x = '' or 99
    print(x)
    # F or F
    x = '' or 0
    print(x)

def transfer():
    answer = input('do you want to transfer all of your money to us (yes/no)? ')
    first_letter = answer[0]
    if first_letter == 'Y' and first_letter == 'y':
        print("nice! transferring...")
    else:
        print('whatever. see ya.')

def ice_cream():
    ans = input("what flavor ice-cream would you like [vanilla]: ")
    # if ans:
    #     flavor = ans
    # else:
    #     flavor = 'vanilla'
    ans = ans or 'vanilla'
    print('one', ans, 'ice-cream comin up!')