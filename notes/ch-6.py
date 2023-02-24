# Functions!
import math
from graphics import Point

# answer = sqrt_9()
# answer = sqrt_16()
answer = math.sqrt(9)

# name
# parameters
# purpose
# return type

# function definition / signature

def add(x, y):
    new_number = x + y
    return new_number

new_value = add(7, 3)
print(new_value)

# function_name(param: data_type) -> return_type (None/Void)
# write a function add(x: int, y: int) -> int that adds two numbers together...

def caesar(sentence, secret_key):
    encrypted_sentence = ''
    for letter in sentence:
        unicode_value = ord(letter)
        encrypted_value = unicode_value + secret_key
        encrypted_letter = chr(encrypted_value)
        encrypted_sentence = encrypted_sentence + encrypted_letter
    return encrypted_sentence

key = 3
x = caesar("the time has come the walrus said", key)
# Variable Scoping
#   Local, Global

# Write a function distance, that returns the distance between two points
def distance(p1, p2):
    term1 = p1.getX() - p2.getX()
    term2 = p1.getY() - p2.getY()
    d = math.sqrt(term1 ** 2 + term2 ** 2)
    return d

click1 = Point(7, 8)
click2 = Point(1, 2)
d = distance(click1, click2)
print(d)

def add_one(my_list):
    new_list = []
    for num in my_list:
        new_list.append(num + 1)
    return new_list

push_ups = [1,2,3,4,5]
add_one(push_ups)
