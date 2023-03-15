from random import randint

def get_campers(lower, upper, number):
    campers = []
    number_of_campers = range(number)
    for i in number_of_campers:
        random_age = randint(lower, upper)
        campers.append(random_age)
    return campers

camper_ages = get_campers(8, 18, 100)
catipillars = []
butterflies = []
eagles = []

for camper_age in camper_ages:
    if camper_age < 10:
        catipillars.append(camper_age)
    elif camper_age < 13:
        butterflies.append(camper_age)
    else:
        eagles.append(camper_age)

# divide everyone randomly into 3 teams
# red, green, blue teams
teams = []
for camper in camper_ages:
    team_number = randint(0, 2)
    if team_number ==  0:
        teams.append('red')
    elif team_number == 1:
        teams.append('green')
    else:
        teams.append('blue')

index = 0
for camper in camper_ages:
    team_color = teams[index]
    if team_color == 'blue':
        pass
        # print(camper, team_color)
    index = index + 1

# lexicographically compared

a = True
b = False
c = False

print(a and b or not c)
# a and b or True
# False or True
# True



