'''
Google maps gives an estimated time of arrival (ETA) whenever directions are requested.
Unfortunately, do to a glitch in their system, the code that performs this calculation
has been deleted and you have been tasked with replacing it. You need to write a program
that asks the user how far they are going and how fast they are going, then print how long
it will take them travel that distance. You remember that given a speed and time, you can
multiply them together to get the distance travelled.
'''

# Strategies for Success!
# 1. Understand the Question
# 2. Specifications
#       input, outputs, formulas
#       (distance, speed), time, speed * time = distance
# 3. Psuedo code! (design)
#       get distance from user
#       convert distance to integer
#       get speed from user
#       convert speed to integer
#       calculate time (time = distance / speed)
#       print the time
# 4. Implementation (code it!)
# 5. Test

def time_calc():
    distance_input = input('enter the distance in miles, please ')
    distance = eval(distance_input)
    speed_input = input('what is your speed in mph? ')
    speed = eval(speed_input)
    time = distance / speed
    print('that will take you', time, 'hours')

name = 'John\nDew\tbury'
print(name)