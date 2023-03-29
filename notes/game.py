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

    # public scope
    def roll(self):
        # self = die2
        random_value = self.__get_random_number()
        self.value = random_value

    # private scope
    def __get_random_number(self):
        return randint(1, self.sides)

class DiceGame:
    # constructor - how to create/start the game
    # game = DiceGame(num_players, winning_score, list_dice )
    #   - number of players
    #   - winning score
    #   - number of dice

    # instance variables - the data stored in the game | what is a game?
    #   - players - list[str] ex: ['player1', 'player2', ...]
    #   - scores - list[int]
    #   - winning score - int
    #   - dice - list[Dice] ex: [Dice(6), Dice(8), ...]
    #   - rounds - int

    # methods - the actions a game can take | what can a game do?
    #   - check for winners
    #   - roll
    #   - check player turn
    #   - report scores
    #   - play
    pass