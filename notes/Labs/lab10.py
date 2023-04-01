from button import Button
from door import Door
from graphics import GraphWin, Rectangle, Point

CLOSED_COLOR = 'yellow'
def main():
    win = GraphWin('Test', 700, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground('white')
    door = Door(Rectangle(Point(3, 7), Point(7, 0)), 'Closed')
    door.color_door(CLOSED_COLOR)
    door.draw(win)
    door_open = False

    door.color_knob('gold')

    button = Button(Rectangle(Point(3, 7.5), Point(7, 9.5)), 'Exit')
    button.draw(win)

    exit_clicked = False
    while not exit_clicked:
        point = win.getMouse()
        exit_clicked = button.is_clicked(point)
        door_clicked = door.is_clicked(point)
        if door_clicked:
            door_open = not door_open
            if door_open:
                door.open('white', 'Open')
            else:
                door.close(CLOSED_COLOR, 'Closed')

if __name__ == '__main__':
    main()
