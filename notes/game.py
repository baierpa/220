from random import randint

class Dice:
    # constructor
    def __init__(self, num_sides):
        self.sides = num_sides
        self.value = num_sides

    # methods
    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def roll(self):
        random_value = randint(1, self.sides)
        self.value = random_value

