import math

from graphics import GraphWin, Polygon, Text, Point, Circle, Entry, color_rgb


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    win.setCoords(0, 0, 10, 10)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    dx1 = p1.getX() - p2.getX()
    dy1 = p1.getY() - p2.getY()
    length1 = math.sqrt(dx1 ** 2 + dy1 ** 2)

    dx2 = p1.getX() - p3.getX()
    dy2 = p1.getY() - p3.getY()
    length2 = math.sqrt(dx2 ** 2 + dy2 ** 2)

    dx3 = p3.getX() - p2.getX()
    dy3 = p3.getY() - p2.getY()
    length3 = math.sqrt(dx3 ** 2 + dy3 ** 2)

    perimeter = length1 + length2 + length3

    s_value = perimeter / 2
    area = math.sqrt(s_value * (s_value - length1) * (s_value - length2) * (s_value - length3))

    perimeter_text = Text(Point(5, 2), "perimeter: " + str(perimeter))
    area_text = Text(Point(5, 1), "area: " + str(area))

    perimeter_text.draw(win)
    area_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry_pt = red_text_pt.clone()
    red_entry_pt.move(40, 0)
    red_entry = Entry(red_entry_pt, 3)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry_pt = green_text_pt.clone()
    green_entry_pt.move(40, 0)
    green_entry = Entry(green_entry_pt, 3)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry_pt = blue_text_pt.clone()
    blue_entry_pt.move(40, 0)
    blue_entry = Entry(blue_entry_pt, 3)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)
    win.getMouse()
    loop_count = range(5)
    for i in loop_count:
        red_value_input = red_entry.getText()
        red_value = eval(red_value_input)
        green_value_input = green_entry.getText()
        green_value = eval(green_value_input)
        blue_value_input = blue_entry.getText()
        blue_value = eval(blue_value_input)
        color = color_rgb(red_value, green_value, blue_value)
        shape.setFill(color)
        win.getMouse()

    # Wait for another click to exit
    win.close()


def process_string():
    user_input = input('enter a string: ')
    print(user_input[0])
    print(user_input[len(user_input) - 1])
    # this can also be user_input[2:6]
    print(user_input[2] + user_input[3] + user_input[4] + user_input[5])
    print(user_input[0] + user_input[len(user_input) - 1])
    first_three = user_input[0] + user_input[1] + user_input[2]
    print(first_three * 10)
    for ch in user_input:
        print(ch)
    print(len(user_input))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * values[0]
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], eval(values[5])]
    print(x)
    x = values[2] + values[0] + eval(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("enter the number of terms: "))
    series = [2, 4, 6]
    total = 0
    for i in range(terms):
        index = i % 3
        value = series[index]
        total = total + value
        print(value, end=' ')
    print()
    print('sum =', total)


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    yellow_radius = 50
    center = Point(win_width / 2, win_height / 2)
    colors = ['yellow', 'red', 'blue', 'black', 'white']
    loops = range(len(colors), 0, -1)
    for i in loops:
        circle = Circle(center, yellow_radius * i)
        circle.setFill(colors[i - 1])
        circle.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def main():
    # triangle()
    # color_shape()
    process_string()
    process_list()
    another_series()
    target()


main()
