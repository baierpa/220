from random import randint

class Dice:
    # constructor
    def __init__(self, num_sides):
        self.sides = num_sides
        self.value = 1

    # methods
    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def roll(self):
        random_number = self.__get_random_number()
        self.value = random_number

    def __get_random_number(self):
        return randint(1, self.sides)
