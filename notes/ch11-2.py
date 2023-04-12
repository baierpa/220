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

print(names[0])
print(names_dictionary[0])

families = {'smith': ['sam', 'sally', 'steve']}
names = families['smith']
print(names)
families['jones'] = ['jane', 'jan', 'jim']
print(families)
families['able'] = ['alan', 'anna', 'ava']
print(families)

# in
family_name = 'smith'
has_family_name = family_name in families
if has_family_name:
    family_members = families[family_name]
    print(f'the {family_name} family exist!')
    print(f'they are: {family_members}')
else:
    print(f'{family_name} family not found')

# keys(), values(), items()
# keys() - returns a sequence of keys from the dictionary
family_names = families.keys()
for key in family_names:
    print(families[key])
# family_names[0] no!
family_names_list = list(family_names)
family_names_list[0]
print('------------------------------------------')
# values()
family_members = families.values()
for member in family_members:
    print(member)
print('-------------------------------------')
# items() - return a sequence of tuples that are key, value pairs
family_unit = families.items()
for family in family_unit:
    last_name = family[0]
    first_names = family[1]
    print(first_names[0])
    print(first_names[1])
