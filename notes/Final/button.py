"""
The Button class represents a clickable button.

Constructor:
    Button(p1: Point, p2: Point, text: string)
        Constructs a button from two points (p1 and p2) and a string of text

Instance Variables:
    shape: Rectangle - The outline of the button
    text: Text - the text of the button (the size can be hardcoded to a constant value like 20)

Methods:
    draw(win: GraphWin) -> None
        Takes a GraphWin object as a parameter and draws the button (all of the button's components) to the win
    undraw() -> None
        Undraws the button (each of the button's components).
    is_clicked(click: Point) -> bool
        Takes a Point object as a parameter and returns True if the point's coordinates are inside the
        button's shape, otherwise returns False
"""