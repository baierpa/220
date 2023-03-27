from graphics import Circle, Point
from game import Dice

p = Point(2, 3)
c = Circle(p, 4)

# DICE
# Instance Variables - what is it/what does it have?
#   - has a number of sides
#   - value
# Methods - what can it do?
#   - roll
#   - get value
# Constructor - how do we make it?
#   - number of sides
# my_die = Dice(6)
# die_value = my_die.get_value()
# print(die_value)
# my_die.set_value(4)
# my_die.roll()
# die_value = my_die.get_value()
# print(die_value)

# Module/class naming conventions
# module - names should be snake_case
# class - name should be PascalCase

die1 = Dice(6)
die2 = Dice(6)

while True:
    input('hit enter to roll')
    die1.roll()
    die2.roll()

    print(die1.get_value())
    print(die2.get_value())