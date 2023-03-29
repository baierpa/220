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

    # public method
    def roll(self):
        # self = die1
        random_number = self.__get_random_number()
        self.value = random_number

    # private method
    def __get_random_number(self):
        return randint(1, self.sides)

class DiceGame:
    # constructor - how to create a DiceGame
    # game = DiceGame(winning_score, num_players)
    # dice?

    # instance variables - what data is in a DiceGame - What is it?
    #   - player scores - list[int]
    #   - dice - list[Dice]
    #   - round - int
    #   - winning score - int
    #   - players - list[str]

    # methods -  what can a DiceGame do?
    #   - tally scores
    #   - rolls the dice
    #   - check for winners
    #   - play
    pass