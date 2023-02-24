# Functions!
import math
from graphics import Point

x = math.sqrt(9)
# y = math.sqrt(16)

# 1. Name
# 2. Purpose
# 3. Parameters
# 4. Return

def add(num, num2):
    new_number = num + num2
    return new_number


x = add(10, 30)
y = add(24, 12)
# y = print(x)
# # None "None"
# print(y)
# function_name(param: data_type) -> return_type (None/Void)
# Write a function add(num: int, num2: int) -> int that adds
# two numbers together...

def caesar(sentence, secret_key):
    # local scope
    encrypted_sentence = ''
    for letter in sentence:
        unicode_value = ord(letter)
        new_number = unicode_value + secret_key
        new_letter = chr(new_number)
        encrypted_sentence = encrypted_sentence + new_letter
    return encrypted_sentence

# variable scope
#   local, global
key = 17
x = caesar('the time has come the walrus said', key)
original = caesar(x, key * -1)

# write a function distance that returns the distance between two points
def distance(p1, p2):
    term1 = p1.getX() - p2.getX()
    term2 = p1.getY() - p2.getY()
    d = math.sqrt(term1 ** 2 + term2 ** 2)
    return d

click1 = Point(2, 3)
click2 = Point(4, 5)
d = distance(click1, click2)
print(d)

def add_one(my_list):
    new_list = []
    for num in my_list:
        new_list.append(num + 1)
    return new_list

push_ups = [1, 2, 3, 4, 5]
correct_push_ups = add_one(push_ups)
print(push_ups)
print(correct_push_ups)