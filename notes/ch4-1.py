from graphics import Point, Circle, GraphWin, Rectangle

# constructor, instance variables, methods

# object
center = Point(5, 5)
my_circle = Circle(center, 2)
win = GraphWin("My Cool Circle!", 700, 700 )

my_x_value = center.getX()
my_y_value = center.getY()

my_circle.draw(win)

win.setCoords(0, 0, 10, 10)
click_point = win.getMouse()
click_x = click_point.getX()
click_y = click_point.getY()
click_point.draw(win)
click_circle = Circle(click_point, 3)
click_circle.setFill('green')
click_circle.setWidth(3)

click_circle.draw(win)


win.getMouse()

# class - the definition of a data type