'''
Google maps gives an estimated time of arrival (ETA) whenever directions are requested.
Unfortunately, do to a glitch in their system, the code that performs this calculation
has been deleted and you have been tasked with replacing it. You need to write a program
that asks the user how far they are going and how fast they are going, then print how long
it will take them travel that distance. You remember that given a speed and time, you can
multiply them together to get the distance travelled.
'''

# 1. Understand the question
# 2. Get Specifications
#       inputs, outputs, formulas
#       distance and speed, time, rate * time = distance
# 3. Pseudo-Code! (design)
#       get user speed
#       convert speed to integer
#       get distance
#       convert distance to integer
#       calculate the time
#       print the time
# 4. Implement/Write the Code
# 5. Test

def time_calc():
    speed_input = input('what is your speed in mph? ')
    speed = eval(speed_input)
    distance_input = input('how far are you going in miles? ')
    distance = eval(distance_input)
    time = distance / speed # r * t = d
    print('that will take you', time,'hours')

# new line character
name = 'John\nDew\tberry'
print(name)