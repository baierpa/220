# Objects and Classes
# Class: definition of a data type
#   1. How to create it - Constructor
#   2. What it is - Instance Variables
#   3. What can it do - Methods
# Object: Instance of a class

from graphics import Point, GraphWin, Text, Entry, Polygon
from time import sleep

win = GraphWin("Points and Thnigs", 500, 500)
win.setCoords(0, 0, 10, 10)
center = Point(5, 2)
# center_two = center
# print("center_two", center_two.getX(), center_two.getY())
# center.move(5, 0)
# print("center", center.getX(), center.getY())
# print("center_two", center_two.getX(), center_two.getY())

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

rocket = Polygon(p1, p2, p3, p4)
rocket.draw(win)
p1.undraw()
p2.undraw()
p3.undraw()
p4.undraw()
frames = range(50)
for i in frames:
    rocket.move(0.2, 0.3)
    sleep(0.5)

# user_input = Entry(Point(5, 8), 10)
# user_input.draw(win)
# win.getMouse()
# user_input_text = user_input.getText()
# instructions.setText(user_input_text)

win.getMouse()



