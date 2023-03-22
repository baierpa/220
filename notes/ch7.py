from random import randint

def is_even(num):
    return num % 2 == 0
# Control Structures

# boolean values
x = True
y = False

# if condition:
#   body

if False:
    print("hello")

age = 23
if is_even(age):
    print("age is even!")

# realtional operators
# < > <= >= == != not
if 3 < 5:
    print("less than!")

# [12, 18, 8, 12, 15,...]
# generate a list of 50 random numbers
def get_campers():
    campers = []
    number_of_campers = range(50)
    for i in number_of_campers:
        random_age = randint(8, 18)
        campers.append(random_age)
    return campers

catipillars = [] # [0-10)
butterflies = [] # [10-13)
eagles = [] # [13-18]

camper_ages = get_campers()
for camper_age in camper_ages:
    if camper_age < 10:
        catipillars.append(camper_age)
    elif camper_age < 13:
        butterflies.append(camper_age)
    else:
        eagles.append(camper_age)

# split into random teams
# red, green, blue
teams = []


for camper in camper_ages:
    team_num = randint(0, 2)
    if team_num == 0:
        teams.append('red')
    elif team_num == 1:
        teams.append('green')
    else:
        teams.append('blue')
index = 0
for camper in camper_ages:
    team_name = teams[index]
    if team_name == 'green':
        print(camper, team_name)
    index = index + 1

# lexicographically compared
