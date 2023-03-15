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

# divide into random teams
# red, green, blue

teams = []
# red = [] # 0
# green = [] # 1
# blue = [] # 2

for camper in campers:
    random_team_number = randint(0, 2)
    if random_team_number == 0:
        teams.append('red')
    elif random_team_number == 1:
        teams.append('green')
    else:
        teams.append('blue')
i = 0
for camper in campers:
    team_color = teams[i]
    if team_color == 'green':
        print(camper, team_color)
    i = i + 1

# lexicographically compared



