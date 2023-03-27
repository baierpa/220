from game import Dice

from graphics import Point, Circle, GraphWin
p = Point(2, 3)

c = Circle(p, 23)
# DICE
# Instance Varibales - the data! what is it? what does it have?
#   - sides
#   - value
# Methods - actions. what can it do?
#   - roll
#   - get value
#   - get sides
#   - set sides
#   - set value
# Constructor - how is a die created?
#   ex: d = Dice(6)
#   - number of sides

# python naming conventions
# modules - names should be snake_case
# class - names should be PascalCase

# die1 = Dice(30)
# die1_value = die1.get_value()
# print(die1_value)
# die1.set_value(2)
# die1_value = die1.get_value()
# print(die1_value)

die1 = Dice(6)
die2 = Dice(6)
while True:
    input('hit enter to roll')
    die1.roll()
    die2.roll()
    print(die1.get_value())
    print(die2.get_value())
