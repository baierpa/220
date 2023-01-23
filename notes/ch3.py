# print
# input

# print('hello, world!', 'how are you?', 'i am great!', 7)
# age = input('what is your age? ')
# age_num = eval(age)
# birth_year = 2023 - age
my_ending = '\t'

print('hi', 'this is another parameter', end='\t')
print('how are you?')

stop = range(5) # generate 0 - 5 (not including 5)
start_stop = range(1, 5) # generate 1 -5 (not including 5)
start_stop_step = range(1, 10, 2) # generate 1-10 by 2s

sum = 0
for my_number in start_stop_step:
    sum = sum + my_number
print(sum)