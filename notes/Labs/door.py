from graphics import Point, Text, Rectangle, Circle


class Door():

    def __init__(self, shape: Rectangle, label):
        self.shape: Rectangle = shape
        self.text = Text(shape.getCenter(), label)
        self.knob = self.__build_knob()
        self.knob.setWidth(0)
        self.secret = False
        self.knob_color = 'gold'

    def __build_knob(self):
        # this can (probably should) be made into a private method
        # need to make it relative to the door size
        # this is not the only way to do this

        # get the right most x value of the door
        # check to see which point is the right one
        rectangle_point_a = self.shape.getP1()
        rectangle_point_b = self.shape.getP2()
        x_a = rectangle_point_a.getX()
        x_b = rectangle_point_b.getX()
        right = x_b
        if x_a > x_b:
            right = x_a

        middle_y = self.shape.getCenter().getY()
        middle_x = self.shape.getCenter().getX()

        # x value of knob will be at 80% from the middle to right side
        # first get the distance from the middle to the right side, then get 80% of that distance
        x_knob = (right - middle_x) * 0.8
        # add the 80% distance to the middle
        x_knob = middle_x + x_knob
        # knob radius will be half of the center to the right side
        knob_radius = (right - x_knob) / 2
        knob_center = Point(x_knob, middle_y)
        return Circle(knob_center, knob_radius)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
        self.knob.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
        self.knob.undraw()

    def is_clicked(self, point):
        # need to get the door's corners and see if the point is in between all the points
        # need to take the absolute value and add it to the center because we do not know which
        # points getP1() and getP2 return - they could be top left, bottom right, or top right, bottom left, etc...

        center = self.shape.getCenter()
        width = abs(self.shape.getP1().getX() - self.shape.getP2().getX())
        height = abs(self.shape.getP1().getY() - self.shape.getP2().getY())
        y_top = center.getY() + height/2
        y_bottom = center.getY() - height/2
        x_left = center.getX() - width/2
        x_right = center.getX() + width/2

        x_point = point.getX()
        y_point = point.getY()

        res = x_left <= x_point <= x_right and y_bottom <= y_point <= y_top
        return res

    def open(self, color, label):
        self.color_door(color)
        self.set_label(label)
        self.knob.setFill(color)

    def close(self, color, label):
        self.color_door(color)
        self.set_label(label)
        self.knob.setFill(self.knob_color)

    def color_door(self, color):
        self.shape.setFill(color)

    def color_knob(self, color):
        self.knob.setFill(color)
        self.knob_color = color

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret


if __name__ == '__main__':
    # Just used for testing...
    rect = Rectangle(Point(4, 2), Point(1, 5))
    # rect = Rectangle(Point(1, 5), Point(4, 2))
    # rect = Rectangle(Point(1, 2), Point(4, 5))
    door = Door(rect, 'me')

    print(door.is_clicked(Point(2, 4)))
