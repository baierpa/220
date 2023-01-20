'''
Google maps gives an estimated time of arrival (ETA) whenever directions are requested.
Unfortunately, do to a glitch in their system, the code that performs this calculation
has been deleted and you have been tasked with replacing it. You need to write a program
that asks the user how far they are going and how fast they are going, then print how long
it will take them travel that distance. You remember that given a speed and time, you can
multiply them together to get the distance travelled.
'''

# Strategies for Success
# 1. Understand the Question
# 2. Specifications
#       inputs, outputs, formulas
#       (distance, speed), time, speed * time = distance
# 3. Pseudo Code! (design)
#       get user distance
#       convert distance to integer
#       get user speed
#       convert speed to integer
#       calculate time - time = distance / speed
#       print the time
# 4. Code it! (implementation)
# 5. Test
# distance_input = input('how far are you going in miles? ')
# distance = eval(distance_input)
# speed_input = input('how fast are you going in mph? ')
# speed = eval(speed_input)
# time = distance / speed
# print('that will take', time, 'hours')

name = "steve\nwalter\tbury"
print(name)

