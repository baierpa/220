from game import Dice
# Lists

# +, *, [], [:], for in, in, len(), sum()

ages = [1,2,3,4,5]
print(sum(ages))

names = ['barry', 'buster', 'bobby', 'belinda']
print(names)
names.sort()
print(names)

def print_dice(dice):
    for die in dice:
        value = die.get_value()
        sides = die.get_sides()
        print(f'Dice({sides})={value}', end=' ')
    print()

def dice_side_sorter(dice):
    return dice.get_sides()

def dice_value_sorter(dice):
    return dice.get_value()


dices = [Dice(9), Dice(32), Dice(17)]
for die in dices:
    die.roll()
print_dice(dices)
dices.sort(key=dice_side_sorter)
print_dice(dices)
dices.sort(key=dice_value_sorter)
print_dice(dices)

# Tuples
ages = (1, 2, 3, 4, 5)
print(ages[1])
print(ages[1:4])
# tuples are immutable!
age_list = [1,2,3,4,5]
age_list[0] = 199
print(age_list)
print(sum(ages))
more_ages = ages + (6,7,8)
print(more_ages * 3)

# dictionaries
# [] - list
# () - tuples
# {} - dictionary

names_list = ['wyatt', 'wendy', 'willy']
names_dictionary = {10000:'wyatt', 200:'wendy', 300:'willy'}

print(names_list[0])
print(names_dictionary[10000])

families = {'smith': ['susan', 'sam', 'steve']}
print(families['smith'])