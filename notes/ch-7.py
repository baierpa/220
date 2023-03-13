from random import randint

def is_even(num):
    return num % 2 == 0

# Control Structures
x = True
y = False
print(x, y)
# if condition:
#   body


if False:
    print('hello')

age = 10
if is_even(age):
    print('that is an even number!')

# relational operators
# < <= > >= == != not
x = 123
if not(9 != 9):
    print("hi")

def get_campers():
    # campers ages
    campers = []
    total_campers = range(50)
    for i in total_campers:
        random_age = randint(8, 18)
        campers.append(random_age)
    return campers

campers = get_campers()
caterpillars = [] # [0-10)
butterflies = [] # [10-13)
eagles = [] # [13-18]

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