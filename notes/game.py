from random import randint

class Dice:
    """
    This represents a Die that would be used in a game
    """
    def __init__(self, num_sides):
        """
        Constructs a Dice object based on num_sides with a default value of 1
        """
        self.sides = num_sides
        self.value = 1

    # methods
    def get_value(self):
        """
        gets the value of the Dice object
        """
        return self.value

    def set_value(self, new_value):
        """
        sets the value of the Dice object (cheater!)
        """
        self.value = new_value

    def roll(self):
        """
        Simulates rolling a Die
        Sets the value to a random number between 1 and the number of sides
        """
        # self = die1
        random_number = self.__get_random_number()
        self.value = random_number

    # private method
    def __get_random_number(self):
        return randint(1, self.sides)

    def get_sides(self):
        return self.sides

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
            print(f'----------------- round {self.round} -----------------')
            scores_index = 0
            for player in self.players:
                input(f"{player}'s turn to roll")
                # rolling the dice
                total_roll = 0
                for die in self.dice:
                    die.roll()
                    total_roll = total_roll + die.get_value()
                    print(die.get_value(), end=' ')
                # setting player score
                player_score = self.scores[scores_index]
                self.scores[scores_index] = player_score + total_roll
                scores_index = scores_index + 1
                print(f'- Total: {total_roll}!')
                if self.game_over():
                    break
            self.__print_summary()
            self.round = self.round + 1
        print('game over!')
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

    def __print_summary(self):
        scores_index = 0
        player_scores = []
        for player in self.players:
            player_scores.append(f'{player}: {self.scores[scores_index]}')
            scores_index = scores_index + 1
        scores_string = ' | '.join(player_scores)
        print(scores_string)
    # methods -  what can a DiceGame do?
    #   - tally scores
    #   - rolls the dice
    #   - check for winners
    #   - play