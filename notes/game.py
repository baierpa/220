from random import randint

class Dice:

    # define constructor
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    # define our methods
    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def roll(self):
        random_value = randint(1, self.sides)
        self.value = random_value