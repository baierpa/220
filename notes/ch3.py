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