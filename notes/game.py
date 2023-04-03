from random import randint

class Dice:
    """
    This class represents a die that can be used in games
    """

    def __init__(self, num_sides):
        """
        Takes the number of sides as a parameter
        Initializes a Dice object with a default value of 1
        """
        self.sides = num_sides
        self.value = num_sides

    def get_value(self):
        """
        gets the value of the Dice
        """
        return self.value

    def set_value(self, new_value):
        """
        sets the value of the Dice (cheater!)
        """
        self.value = new_value

    # public scope
    def roll(self):
        """
        rolls the Dice, setting its value to a random number between 1 and the number of sides
        """
        # self = die2
        random_value = self.__get_random_number()
        self.value = random_value

    # private scope
    def __get_random_number(self):
        return randint(1, self.sides)

class DiceGame:
    # constructor - how to create/start the game
    def __init__(self, number_players, winning_score, dice):
        self.round = 1
        self.winning_score = winning_score
        self.dice = dice
        self.players = []
        self.scores = []
        player_range = range(number_players)
        # register players and start scores at 0
        for i in player_range:
            self.players.append(f'player{i + 1}')
            self.scores.append(0)

    def play(self):
        while not self.__game_over():
            print(f'-------------- round {self.round} --------------')
            player_index = 0
            for player in self.players:
                input(f"{player}'s turn to roll")
                # roll the dice
                total = 0
                for die in self.dice:
                    die.roll()
                    total = total + die.get_value()
                    print(die.get_value(), end=' ')
                print(f'- total: {total}')
                # adding player score
                player_score = self.scores[player_index]
                self.scores[player_index] = player_score + total
                player_index = player_index + 1
                if self.__game_over():
                    break
            self.__print_scores()
            self.round = self.round + 1
        print('Game over!')
        # while the game is not over
        #   print the round
        #   for each player
        #       tell them to roll
        #       roll the dice
        #       for each die
        #             print its value
        #             sum the values
        #         print the total roll
        #         check if the game is over
        #   print game report

    def __game_over(self):
        for score in self.scores:
            if score >= self.winning_score:
                return True
        return False

    def __print_scores(self):
        player_scores = []
        index = 0
        for player in self.players:
            new_string = f'{player}: {self.scores[index]}'
            player_scores.append(new_string)
            index = index + 1
        print(' | '.join(player_scores))
    # game = DiceGame(num_players, winning_score, list_dice)
    #   - number of players
    #   - winning score
    #   - list of dice
    #   - rounds

    # instance variables - the data stored in the game | what is a game?
    #   - players - list[str] ex: ['player1', 'player2', ...]
    #   - scores - list[int] ex: [0, 0, 0, ...]
    #   - winning score - int
    #   - dice - list[Dice] ex: [Dice(6), Dice(8), ...]
    #   - rounds - int

    # methods - the actions a game can take | what can a game do?
    #   - check for winners
    #   - roll
    #   - check player turn
    #   - report scores
    #   - play