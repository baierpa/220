from game import DiceGame, Dice

d1 = Dice(6)
d2 = Dice(8)
dice = [d1, d2]
our_game = DiceGame(dice, 4, 20)
our_game.play()