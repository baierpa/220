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

root_9 = math.sqrt(9)
power = math.pow(3, 2)
print(root_9)
print(power)

