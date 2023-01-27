import math

# print
# input

# print('hello, world!', 'how are you?', 'i am great!', 7)
# age = input('what is your age? ')
# age_num = eval(age)
# birth_year = 2023 - age
my_ending = '\t'

# print('hi', 'this is another parameter', end='\t')
# print('how are you?')

stop = range(5) # generate 0 - 5 (not including 5)
start_stop = range(1, 5) # generate 1 -5 (not including 5)
start_stop_step = range(1, 10, 2) # generate 1-10 by 2s

sum = 0
for my_number in start_stop_step:
    sum = sum + my_number
# print(sum)

# ten_range = range(100, 110)
# for i in ten_range:
#     # body
#     print('hey!', end='\t')
# print('done!')

# age = 43
# next_ten = range(1, 11)
# for year in next_ten:
#     new_age = age + year
#     print('in', year, 'years, you will be', new_age, 'years old')
# print('wow, you will be super old in 10 years')

# nested loops
outer_five = range(1, 6)
inner_five = range(1, 6)

# for j in outer_five:
#     for i in inner_five:
#         print(i + j, end='\t')
#     print()

# + - * / **
result = math.sqrt(9)
print(result)
# dot notation
print(math.pi)
print(math.e)
power = math.pow(4, 7) # 4 ** 7\

# float - numbers with decimals
# + - * / **
# ints -> ints, floats -> floats, int & float -> float
res = 3 * 7
print(res)
range(res)

res = 3.0 * 7.0
print(res)

res = 3.0 + 7
print(res)

# EXCEPT! /
res = 6 / 2 # floating point division operator
print(res)

res = 6 // 2 # integer division operator
print(res)

res = 7 // 2 # truncates!
print(res)

res = 7.5 // 2 # truncates!
print(res)

# int(), float()
my_int = int(4.7)
print(my_int)

my_float = float(7)
print(my_float)

print(7 * 1.0)

# round()
x = round(4.7) # >= 5 rounds up
print(x)
x = round(4.4) # < 5 rounds down
print(x)

x = round(4.7, 2)
print(x)

x = round(4.509, 2)
print(x)

# + - * / // **

# % - mod - modulus - modulo -> remainder operator

months = range(120)
for i in months:
    month_num = (i % 12) + 1
    print(month_num, end=' ')