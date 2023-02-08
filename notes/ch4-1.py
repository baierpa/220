from graphics import Point, Circle, GraphWin, Line

# contruction, instance variables, methods

# object
center = Point(5, 5)
my_circle = Circle(center, 2)
win = GraphWin("My Cool Circle!", 700, 700)
win.setCoords(0, 0, 10, 10)

center_x = center.getX()
center_y = center.getY()

my_circle.draw(win)

click_point = win.getMouse()
circle_click = Circle(click_point, 3)
circle_click.draw(win)
circle_click.setFill("green")
circle_click.setWidth(3)
circle_click.setOutline("purple")

win.getMouse()

# class - defines a data type