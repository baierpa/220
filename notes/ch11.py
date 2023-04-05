from game import Dice
from random import randint, uniform
# Collections (data structures)


def get_random_nums(x, is_floats):
    """
    returns a random list of floats that is x elements long
    if is_floats is true, the list should be floast, otherwise ints
    """
    our_list = []
    r = range(x)
    for i in r:
        if is_floats:
            random_num = uniform(0, 100)
        else:
            random_num = randint(0, 100)
        our_list.append(random_num)
    return our_list

# Lists
# initialize
ages = [1, 2, 3, 4, 5]
names = ["sue", "sam", "steve"]
data = [1, "hello", 2, "world"]
dice = [Dice(12), Dice(8), Dice(10)]

# accessing list elements
# indexing
sam = names[1]
# loop
for name in names:
    print(name)

# operators - +, *, [], [:], len, for in, in
# + - concat
combo = [1,2,3] + [4,5,6] # returns a single list
print(combo)
# * - repetition
repeat = ['hello', 'world'] * 3 # returns a single list
print(repeat)
# indexing
# combo[6] # error if index out of range
# slicing
part_of_combo = combo[1:5] # start:stop:step
print(part_of_combo)
combo_length = len(part_of_combo) # returns the number of items in a list
print(combo_length)
# in - membership check
three_in_list = 3 in part_of_combo # returns a boolean value
if 7 in part_of_combo:
    print('has seven!')
else:
    print('no sevens :(')

# methods
temps = get_random_nums(100, True)
ages = get_random_nums(100, False)

print(ages)
ages.append(100)
print(ages)

ages.sort()
print(ages)
names = ["sue", "sam", "steve"]
names.sort()
print(names)
dice = [Dice(12), Dice(8), Dice(10)]

names.reverse()
print(names)

i = names.index('sam')
print(i)

names.insert(10, 'sloan')
print(names)

tens = ages.count(10)
print(tens)

# print(ages)
# ages.remove(10)
# print(ages)

last_one = names.pop(1)
print(names)
print(last_one)

def print_dice(dice_list):
    for die in dice_list:
        print(die.get_sides(), end=' ')
    print()

def dice_sort_sides(dice):
    return dice.get_sides()

def dice_sort_value(dice):
    return dice.get_value()


print_dice(dice)
dice.sort(key=dice_sort_sides)
print_dice(dice)

dice.sort(key=dice_sort_value)
print_dice(dice)
