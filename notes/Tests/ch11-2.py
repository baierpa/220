from game import Dice
# lists

# +, *, [], [:], for in, in, len(), sum()

ages = [1,2,3,4,5]
total = sum(ages)
print(total)

# sort

names = ['alex', 'ann', 'aaron']
print(names)
names.sort()
print(names)

def print_dice(dice):
    for die in dice:
        print(f'Dice({die.get_sides()})', end=' ')
    print()

def dice_sort_sides(dice):
    return dice.get_sides()

def dice_sort_value(dice):
    return dice.get_value()


dices = [Dice(9), Dice(2), Dice(4)]

print_dice(dices)
# [9, 2, 4]
dices.sort(key=dice_sort_sides)
print_dice(dices)
for die in dices:
    die.roll()
dices.sort(key=dice_sort_value)
print_dice(dices)

# tuples - immutable!
my_favorite_numbers = (4, 12, 99, 43, 23)
print(my_favorite_numbers[1])
print(my_favorite_numbers[1:4])
# my_favorite_numbers[1] = 100 NO!
new_favs = my_favorite_numbers + (101, 102)
print(new_favs * 4)

# dictionaries
# [] - lists
# () - tuples
# {} - dictionary
names = ['Jane', 'John', 'Joan']
names_dictionary = {1:'Jane', 100:'John', 200:'Joan'}

print(names[0], names_dictionary[200])

families = {'smith': ['steve', 'sam', 'sean'], 'jones': ['jane', 'jim', 'john']}
families['johnson'] = ['jordan', 'jackson', 'jason']
smith_family = families['smith']
jones_family = families['jones']
print(smith_family)
for person in smith_family:
    print(f'hi {person}!')

# explain on wednesday! have a great test!
families.items()
families.keys()
families.values()

