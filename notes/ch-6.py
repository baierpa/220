# Functions!
import math
from graphics import Point

# x = 9
# y = math.sqrt(x)
# z = math.sqrt(y)
# parts of a function
# 1. name
# 2. parameters     1 and 2 are called the Function Signature/Definition
# 3. body
# 4. return value

def add(number, number2):
    new_number = number + number2
    return new_number

x = add(10, 15)
# None
y = print(x)

def caesar(message, secret_key):
    # local scope
    encrypted_string = ''
    for letter in message:
        letter_value = ord(letter)
        new_letter_value = letter_value + secret_key
        new_letter = chr(new_letter_value)
        encrypted_string = encrypted_string + new_letter
    return encrypted_string

caesar('the time has come the walrus said', 4)

x = caesar('the time has come the walrus said', 4)
# y = caesar("hello world!", 9)
# original = caesar(x, -4)
# print(original)

# function_name(param: type) -> return_type (None/Void)
# Write a function caesar(message: string, key: int) -> string that encrypts the message with the key...

# Variable Scope
# local vs. global

# write a function distance that calculates the distance between two points
def distance(p1, p2):
    term1 = p1.getX() - p2.getX()
    term2 = p1.getY() - p2.getY()
    d = math.sqrt(term1 ** 2 + term2 ** 2 )
    return d

click1 = Point(2, 3)
click2 = Point(6, 7)
click_distance = distance(click1, click2)
print(click_distance)

# does not mutate
def add_one(my_list):
    resulting_list = []
    for num in my_list:
        resulting_list.append(num + 1)
    return resulting_list

# mutates!
def add_one_mutator(my_list):
    indexes = range(0, len(my_list))
    for i in indexes:
        my_list[i] = my_list[i] + 1
    return my_list

push_ups = [1,2,3,4,5]

add_one(push_ups)
print(push_ups)

add_one_mutator(push_ups)
print(push_ups)

# parameters vs arguments