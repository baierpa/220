import math

# print, input
# print("this is what i'm printing", "see here", "and another", end="\n\n")
# print('this is another line')

up_to_four = range(5) # stop at 5
start_stop = range(2, 5) # start at 2, stop at 5
start_stop_step = range(1, 10, 2) # start at 1, stop at 10, count by 2s
# print(up_to_four)


# for each_number in up_to_four:
#     print(each_number)
#
# for i in start_stop:
#     print(i)

sum = 0
for i in start_stop_step:
    sum = sum + i
# print(sum)

age = 43
my_numbers = range(1, 11)
for number in my_numbers:
    new_age = age + number
    # print("In", number, "years, you will be", new_age, "years old.")
# print('wow, you will be really old in 10 years')

# nested loops
five_range = range(1, 6)
another_range = range(1, 6)
for i in five_range:
    for j in another_range:
        print(j + i, end='\t')
    print()

# + - * / **

# dot notation

print(math.e)
print(math.pi)

# return floats
root_9 = math.sqrt(9)
power = math.pow(3, 2)
print(root_9)
print(power)

# floats
#  + - * /
# ints -> ints, floats -> floats, int & float -> float
res = 4 * 1.0
print(res)

# exception / -> always float
# floating point division
res = 6 / 2
print(res)
# integer division
res = 6 // 2
print(res)

res = 4 * 1.3
res_int = int(res)
print(res_int)
# truncating decimals
print(int(3.9))

num = float(34)
print(num)

bound = int(3/1)
range(bound)

x = 3.7
rounded_x = round(x)
print(rounded_x)

x = 3.72346452
rounded_x = round(x, 4)
print(rounded_x)

# + - * / // **
# % mod - modulo - modulus
mod_result = 4 % 3
print(mod_result)

numbers = range(144)
for i in numbers:
    month_number = (i % 12) + 1
    print(month_number, end=' ')

'''
Write a function that asks a user to enter an integer n,
calculates the sum of n terms in the series below, then prints the resulting sum.
For example:
    a user entering 1 would print 1.0 or
    a user entering 2 would print 1.6666666666666665.

*Note the series is not given to you.

3/3 + 4/6 + 5/9 + 6/12 + 7/15 + …
'''
