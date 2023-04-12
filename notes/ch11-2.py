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

# print(names[0], names_dictionary[200])

families = {'smith': ['steve', 'sam', 'sean'], 'jones': ['jane', 'jim', 'john']}
# adding to a dictionary
families['johnson'] = ['jordan', 'jackson', 'jason']
# referencing values in a dictionary
smith_family = families['smith']
jones_family = families['jones']
# print(smith_family)
# for person in smith_family:
#     print(f'hi {person}!')

for last_name in families:
    names = families[last_name]
    print(f'in the {last_name} familes are: ')
    print(f'\t{names}')

if 'smith' in families:
    print('hi smiths!')

# keys() - returns a sequence of keys
family_last_names = families.keys()
family_last_names_list = list(family_last_names)
for name in family_last_names:
    print(families[name])

# values() - returns a sequence of values
family_members = families.values()
for people in family_members:
    print(people)
# can't index .values()
# family_members[0] error! con't index dict_values
family_members_list = list(family_members)
names = family_members_list[0]
print(names)

# items() - returns a sequence of tuples of key/value pairs
# {'smith': ['steve', 'sam', 'sean'], 'jones': ['jane', 'jim', 'john'], 'johnson': ['jordan', 'jackson', 'jason']}
# [ ('smith', ['steve', 'sam', 'sean']), ('jones', ['jane', 'jim', 'john']), ('johnson', ['jordan', 'jackson', 'jason']) ]
pairs = families.items()
for pair in pairs:
    last_name = pair[0]
    members = pair[1]
    print(f'{last_name}')
    for name in members:
        print(f'\t{name}')

print(families)
# families.clear()
# del(families['jones'])
# print(families)
# a = families['jones1']
b = families.get('jones1', ['a', 'b', 'c'] )
# print(a)
print(b)