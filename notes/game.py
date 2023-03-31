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
    def __init__(self, winning_score, num_players, dice):
        self.round = 1
        self.winning_score = winning_score
        self.dice = dice
        self.scores = []
        self.players = []
        player_range = range(num_players)
        # player registration
        for number in player_range:
            self.scores.append(0)
            self.players.append(f'player{number + 1}')

    # constructor - how to create a DiceGame
    # game = DiceGame(winning_score, num_players, num_dice)
    # dice?

    # instance variables - what data is in a DiceGame - What is it?
    #   - player scores - list[int] ex: [0, 0, ...]
    #   - dice - list[Dice]
    #   - round - int
    #   - winning score - int
    #   - players - list[str] ex: ["player1", "player2", ...]

    def play(self):
        while not self.game_over():
            # test game over!
            print(self.scores)
        # while the game not over
        #   print the round
        #   for each player
        #       print the player
        #       player rolls (hits enter)
        #       for each dice
        #           roll
        #           get/print the value
        #           add value to sum
        #       print total
        #       add total to player's score
        #       check if the game is over
        #   print game summary

    def game_over(self):
        for score in self.scores:
            if score >= self.winning_score:
                return True
        return False

    # methods -  what can a DiceGame do?
    #   - tally scores
    #   - rolls the dice
    #   - check for winners
    #   - play
    pass