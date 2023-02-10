# Classes and Objects
# Class - defines a new data type
#   1. Constructor
#   2. Instance Variables - the data (what is it?)
#   3. Methods - actions (what does it do?)
# Object - an instance of a class

from graphics import Point, GraphWin, Text, Entry, Polygon
from time import sleep

win = GraphWin("My Cool Window", 500, 500)
win.setCoords(0, 0, 10, 10)

center = Point(5, 9)

instructions = Text(center, "Click 4 points")
instructions.draw(win)

p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
p4 = win.getMouse()
p4.draw(win)

p1.undraw()
p2.undraw()
p3.undraw()
p4.undraw()

rocket = Polygon(p1, p2, p3, p4)
rocket.draw(win)

frames = range(50)
for i in frames:
    rocket.move(0.2, 0.3)
    sleep(0.1)

win.getMouse()

# print("center", center.getX(), center.getY())
# center_copy = center.clone()
# print("center_copy", center_copy.getX(), center_copy.getY())
#
# center.move(3, 2)
#
# print("center", center.getX(), center.getY())
# print("center_copy", center_copy.getX(), center_copy.getY())


# win = GraphWin("My Cool Window", 500, 500)
# win.setCoords(0, 0, 10, 10)
#
# center = Point(5, 9)
#
# instructions = Text(center, "Click 4 points")
# instructions.draw(win)
# user_input = Entry(Point(5, 1), 15)
# user_input.draw(win)
#
# win.getMouse()
#
# user_input_text = user_input.getText() # input
# instructions.setText(user_input_text)
#
# win.getMouse()



# center.draw(win)
# win.getMouse()
# center.move(0, -8)
# win.getMouse()
