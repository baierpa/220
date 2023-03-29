from game import Dice

from graphics import Point, Circle
p = Point(3, 4)

c = Circle(p, 23)
c.move(2, 3)
# Dice
# Instance variables - Data! what is it? what does it have?
#   - number of sides
#   - value
# Methods - actions. what can it do?
#   - roll
#   - get the value
#   - get number of sides
#   - set number of side
# Constructor - how to build it
#   number of sides
#   d = Dice(6)

# naming conventions
# modules - name should snake_case

# classes - name should PascalCase

# die1 = Dice(6)
# die1.set_value(3)
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