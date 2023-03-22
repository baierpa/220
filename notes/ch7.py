from random import randint

# Control Structures
# Conditional
# booleans
x = True
y = False
# if condition:
#   body


if y:
    print('yay!')

def is_even(num):
  return num % 2 == 0

if is_even(4):
    print('yeah, that is even!')

# Relational Operators
# < > <= >= == != not
print(3 < 7)
if 7 == 7:
    print('ok')

# get campers ages
# for each camper check if even/odd
# if even, move left
# if odd, move right

def get_campers():
    campers = []
    number_of_campers = range(50)
    for i in number_of_campers:
        random_age = randint(8, 18)
        campers.append(random_age)
    return campers

caterpillars = [] # up to age 10 (not including 10)
butterflies = [] # age 10 - 13 (not including 13)
eagles = [] # age 13 and over

campers = get_campers()
for camper_age in campers:
    if camper_age < 10:
        caterpillars.append(camper_age)
    elif camper_age < 13:
        butterflies.append(camper_age)
    else:
        eagles.append(camper_age)
print(caterpillars)
print(butterflies)
print(eagles)


