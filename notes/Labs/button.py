from graphics import Point, Text, Rectangle


class Button():

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        # need to get the button's corners and see if the point is in between all the points
        # need to take the absolute value and add it to the center because we do not know which
        # points getP1() and getP2 return - they could be top left, bottom right, or top right, bottom left, etc...
        center = self.shape.getCenter()
        width = abs(self.shape.getP1().x - self.shape.getP2().x)
        height = abs(self.shape.getP1().y - self.shape.getP2().y)
        y_top = center.y + height/2
        y_bottom = center.y - height/2
        x_left = center.x - width/2
        x_right = center.x + width/2

        x_point = point.getX()
        y_point = point.getY()

        res = x_left <= x_point <= x_right and y_bottom <= y_point <= y_top
        return res

    def color_button(self, color):
        self.shape.setFill(color)



if __name__ == '__main__':
    # Just used for testing...
    rect = Rectangle(Point(4, 2), Point(1, 5))
    # examples of different Point orders potentially causing issues with is_clicked if not handled properly
    # rect = Rectangle(Point(1, 5), Point(4, 2))
    # rect = Rectangle(Point(1, 2), Point(4, 5))
    button = Button(rect, 'me')

    print(button.is_clicked(Point(2, 4)))
