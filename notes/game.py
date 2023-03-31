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
        self.dice = game_dice
        self.scores = []
        self.players = []
        player_range = range(num_players)
        for i in player_range:
            self.scores.append(0)
            self.players.append(f'player{i + 1}') # player1, player2, ...

    def play(self):
        while not self.__game_over():
            print(f'round {self.round}')
            player_index = 0
            for player in self.players:
                input(f'{player} turn to roll')
                # roll
                total = 0
                for die in self.dice:
                    die.roll()
                    print(die.get_value(), end=' ')
                    total = total + die.get_value()
                self.scores[player_index] = self.scores[player_index] + total
                print(f' - total roll: {total}')
                player_index = (player_index + 1) % len(self.players) # ensures index is always in range
                if self.__game_over():
                    break
            self.round = self.round + 1
        # while game is not over
        #   print the round
        #   for each player
        #       print the player's name
        #       player rolls
        #       total their roll
        #       print their roll
        #       check if anyone won

    def __game_over(self):
        for score in self.scores:
            if score >= self.end_score:
                return True
        return False

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