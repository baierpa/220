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
        # self = die1
        random_value = self.__get_random_value()
        self.value = random_value

    def __get_random_value(self):
        return randint(1, self.sides)


class DiceGame:
    #  constructor
    def __init__(self, game_dice, num_players, end_score):
        self.round = 1
        self.end_score = end_score

    #   game_dice = [Dice(6)]
    #   game = DiceGame(game_dice, number of players, end score)
    #   how do we initialize/start?
    #       - number dice
    #       - number of players
    #       - end score

    # instance variables
    #   what is a game? what data does it store?
    #       - player scores (list[int])
    #       - players (list[str]) - ex: ["player1", "player2"...]
    #       - round (int)
    #       - end score (int)
    #       - dice (list[Dice])

    # methods
    #   what does a game do?
    #       - play
    #       - report the scores
    #       - rolls
    #       - check for winners
    pass