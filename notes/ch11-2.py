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
names_dictionary = {10000:'wyatt', 200:'wendy', 300:'willy'} # key:value

# referencing values
print(names_list[0])
print(names_dictionary[10000])

families = {'smith': ['susan', 'sam', 'steve']}
# {'smith': ['susan', 'sam', 'steve']}
print(families)
names = families['smith']
print(names)
# insert into dictionary
families['jones'] = ['jerry', 'jane', 'jim']
# {'smith': ['susan', 'sam', 'steve'], 'jones': ['jerry', 'jane', 'jim']}
print(families)
families['able'] = ['aaron', 'ada', 'al']

# in
has_smith = 'smith' in families
if has_smith:
    print('hey smith family!')

last_name = 'jones'
print(families[last_name])

# keys(), values(), items()
# keys() - return a sequence of keys from the dictionary
last_names = families.keys()
for last_name in last_names:
    value = families[last_name]
    print(f'Introducing the {last_name} family!')
    print(f'\t{value}')

# last_names_list = list(last_names)
# smith = last_names_list[0]
# print(smith)

# values() - return a sequence of values from the dictionary
names = families.values()
for name in names:
    for person in name:
        print(person, end='---')
    print()
names_list = list(names)
names_list[0]

# items - return a sequence of tuples containing key, value pairs
familiy_members = families.items()
for family in familiy_members:
    last_name = family[0]
    members = family[1]
    print(f'The {last_name} family!')
    print(f'\t{members}')

for family in families:
    print(f'{family}!!!')

# families.clear()
# print(families)

# del(families['jones'])
# print(families)

ables = families.get('ables',  ['a', 'b', 'c'])
print(ables)
stocks = {'abc': None}
print(stocks)
stocks['abc'] = 'something'
print(stocks)