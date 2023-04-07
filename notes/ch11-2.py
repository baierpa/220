from game import Dice
# List

# +, *, [], [:], for in, in, len(), sum()

ages = [1,2,3,4,5]
print(sum(ages))

names = ['nancy', 'nina', 'nelly', 'nick']
print(names)
names.sort()
print(names)

def print_dice(dice):
    for die in dice:
        sides = die.get_sides()
        value = die.get_value()
        print(f'Dice({sides})={value}', end=' ')
    print()
def sort_dice_sides(dice):
    return dice.get_sides()

def sort_dice_values(dice):
    return dice.get_value() * -1

dices = [Dice(19), Dice(16), Dice(23)]
for die in dices:
    die.roll()
# higher order function
dices.sort(key=sort_dice_sides)
print_dice(dices)
dices.sort(key=sort_dice_values)
print_dice(dices)

# Tuples
# ()
ages = (1,2,3,4,5)
ages_list = [1,2,3,4,5]
print(len(ages))
print(sum(ages))
print(ages[3])
print(ages[1:4])
print((1,2,3) + (4,5,6))

# tuples are immutable!
# ages[0] = 100

# Dictionaries!
# [] - lists
# () - tuples
# {} - dictionary
names = ['harry', 'halie', 'heather']
names_dictionary = {0: 'harry', 1: 'halie', 2: 'heather'}
