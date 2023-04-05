from game import Dice
from random import uniform, randint
# Data Structures
# Collections
# Lists

def get_random_float_list(x):
    r = range(x)
    list_of_numbers = []
    for i in r:
        list_of_numbers.append(uniform(0, 100))
    return list_of_numbers

def get_random_int_list(x):
    r = range(x)
    list_of_numbers = []
    for i in r:
        list_of_numbers.append(randint(0, 100))
    return list_of_numbers


# initialize a list
ages = [1, 2, 3, 4, 5, 6, 7]
names = ["sam", "susan", "steve"]
dice = [Dice(16), Dice(8), Dice(10)]
data = [1, "hi", 2, "world"]

# accessing elements of a list
# indexing
sue = names[2]
ten = dice[2]
print(ten.get_value())
print(dice[2].get_value())

# for item in data:
#     print(item, end=' ')

# operators - + (concat), * (repetition), [] indexing, len, [:] slicing, for in, in
combo = names + dice # combines the lists into a single list
repeat = names * 2 # returns a single list
print(len(combo))
ages = [1, 2, 3, 4, 5, 6, 7]
part_of_ages = ages[1:5] # returns a new list
print(part_of_ages)
has_five = 5 in ages # membership check - returns boolean
print(has_five)
if 12 in ages:
    print('has 12')
else:
    print('nobody is 12')

# methods - mutate the list
print(ages)
ages.append(8)
print(ages)
temps = get_random_float_list(100)
# sort
print(temps)
temps.sort()
print(temps)
temps.reverse()
print(temps)
ages = get_random_int_list(100)
print(ages)
i = ages.index(7) # will error if not found
print(i)
sevens = ages.count(7)
print(sevens)
ages.remove(7) # errors if not found
print(ages)
days = get_random_int_list(10)
print(days)
last_one = days.pop() # removes and returns
print(days, last_one)
first_one = days.pop(0)
print(first_one, days)

# sorting
print(names)
names.sort()
print(names)

def sort_by_sides(dice):
    return dice.get_sides()

def sort_by_value(dice):
    return dice.get_value()

# higher order function

dice.sort(key=sort_by_value)
for die in dice:
    print(die.get_value(), end=' ')

