# libraries
import math

# print
# input

# print("hi", 7, "how are you?", "what is your name?" )
# age = input("enter your age: ")
# birth_year = 2023 - age

print("hi", end="\t")
print("how are you?")

stop = range(5) # generate 0 - 4
start_stop = range(1, 5) # generate 1 - 4
start_stop_step = range(1, 10, 2) # generate 1 - 9

sum = 0
for num in stop:
    sum = sum + num
# print(sum)

one_to_ten = range(1, 11)
# for one_number in one_to_ten:
#     # body
#     print(one_number)
# print('done!')

ten_range = range(100, 110)
for i in ten_range:
    print('hey!', end=' ')
print()

# age = 43
# next_ten = range(1, 11)
# for year in next_ten:
#     new_age = age + year
#     print('after', year, 'year(s) you will be', new_age, 'years old!')
# print('wow, you will be really old after 10 years!')
# print(age)
#
# for j in range(10):
#     age = age + 1
#     print(age)
# print(age)

# nested loops
one_to_five_outer = range(1, 11)
one_to_five_inner = range(1, 5)
for i in one_to_five_outer:
    for j in one_to_five_inner:
        print(i + j, end='\t')
    print()

# + - * / **
math.sqrt(9)
#  dot notation
print(math.pi)
print(math.e)
result = math.pow(3, 4) # 3 ** 4
print(result)

# floating point data type
x = 3.4
y = 3
# + - * /
res = 2.5 + 5.9
print(res)
# ints -> int, floats -> float, int & float -> float
print(3 * 5)
print(3.0 * 5.9)
print(3 + 4.7)
print(3 + 4.0)
# exception! / division
res = 6 / 3 # / floating point division operator
print( res )
res = 6 // 3 # // integer divsion operator
range(res)
print(res)

res = 6.7 // 3 # truncated result
print(res)

# int(), float()
my_int = int(6 / 2)
print(my_int)

my_float = float(7)
print(my_float)

my_int = int(3.7)
print(my_int)

# round()
res = round(4.49384039874) # round down <= .5
print(res)
res = round(4.5100000) # round up > .5
print(res)
res = round(4.97898769, 3)
print(res)

# + - * / // **
# % mod - modulus - modulo -> remainder operator

month_nums = range(144)
for month in month_nums:
    month_num = (month % 12) + 1
    print(month_num, end=' ')

'''
Write a function that asks a user to enter an integer n,
calculates the sum of n terms in the series below, then prints the resulting sum.
For example:
    a user entering 1 would print 1.0 or
    a user entering 2 would print 1.6666666666666665.

*Note the series is not given to you.

3/3 + 4/6 + 5/9 + 6/12 + 7/15 + …
'''
print()
n_input = input('how many terms should we add? ')
n = eval(n_input)
terms = range(n)
total = 0
num = 2
den = 0
for i in terms:
    num = num + 1
    den = den + 3
    total = total + num / den
print(total)