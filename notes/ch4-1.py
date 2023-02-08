from graphics import Point, Circle, Rectangle, GraphWin, Polygon

# construct, instance variables, methods
# constructor
center = Point(5, 5) # creates an object
my_circle = Circle(center, 1)
win = GraphWin("My Cool Circle", 700, 700)

center_x = center.getX()
center_y = center.getY()

# Class - the definition of a data type

my_circle.draw(win)
win.setCoords(0, 0, 10, 10)

ceneter_circle_2 = win.getMouse()
circle_2 = Circle(ceneter_circle_2, 3)
circle_2.setWidth(3)
circle_2.setFill('red')
circle_2.setOutline("blue")
circle_2.draw(win)

p1 = win.getMouse()
p2 = win.getMouse()
my_rectangle = Rectangle(p1, p2)
my_rectangle.setFill("purple")
my_rectangle.draw(win)

poly = Polygon(p1, p2, center)
poly.setFill("yellow")
poly.draw(win)

win.getMouse()

