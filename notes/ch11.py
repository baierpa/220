# collections (data structures)
from game import Dice
from random import randint, uniform

def make_random_numbers(x, is_float):
    """
    return a list of random numbers
    x is the number of elements in the list
    if is_float is True, the list will be all floats, otherwise all ints
    """
    my_list = []
    r = range(x)
    for i in r:
        if is_float:
            random_num = uniform(0, 100)
        else:
            random_num = randint(0, 100)
        my_list.append(random_num)
    return my_list

# List
# initialize
ages = [1,2,3,4]
names = ["sue", "steve", "sam"]
data = [1, "hello", 2, "world"]
dice = [Dice(18), Dice(10), Dice(14)]

# referencing elements in a list
# indexing
steve = names[1]
ten = dice[1]
ten.roll()
print(dice[1].get_value())
print(ten.get_value())

# loop
# for age in ages:
#     print(age, end=' ')

# operators
# +, *, [], [:], len, for in, in

# + concat
combo = [1,2,3,4] + [5, 6] # returns a single, new list
print(combo)
# * repetition
multi_names = names * 3 # returns a single, new list
print(multi_names)
# slicing
part_of_combo = combo[1:5] #start:stop:step
print(part_of_combo)
# len()
size = len(combo)
print(size)
# in - membership check
has_steve = "steve" in names # returns a boolean
print(has_steve)
has_ten = ten in dice
print(has_ten)
if "scott" in names:
    print('hey steve')
else:
    print('stranger')

# methods
ages = make_random_numbers(100, False)
temps = make_random_numbers(100, True)

print(ages)
print(temps)

ages.append(100)
print(ages)

ages.sort()
print(ages)
names = ["sue", "steve", "sam"]
names.sort()
print(names)
# dice.sort()

names.reverse()
print(names)

i = names.index('steve')
print(i)

names.insert(10, "scott")
print(names)

c = ages.count(10)
print(c)
print(ages.index(10))
print(ages)
ages.remove(10)
print(ages)

last_one = names.pop(1)
print(names, last_one)