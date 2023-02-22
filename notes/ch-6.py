# Functions!
import math

# x = 9
# y = math.sqrt(x)
# z = math.sqrt(y)
# parts of a function
# 1. name
# 2. parameters     1 and 2 are called the Function Signature/Definition
# 3. body
# 4. return value

def add_number_plus_one(number):
    new_number = number + 1
    return new_number

x = add_number_plus_one(10)
x = add_number_plus_one(x)
print(x)


