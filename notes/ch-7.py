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

from random import randint

def get_campers():
    campers = []
    number_of_campers = range(50)
    for i in number_of_campers:
        random_age = randint(8, 16)
        campers.append(random_age)
    return campers

all_campers = get_campers()
left = []
right = []
for camper in all_campers:
    if camper % 2 == 0:
        left.append(camper)
    if camper % 2 == 1:
        right.append(camper)
print(left)
print(right)

