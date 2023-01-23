# print, input
# print("this is what i'm printing", "see here", "and another", end="\n\n")
# print('this is another line')

up_to_four = range(5) # stop at 5
start_stop = range(2, 5) # start at 2, stop at 5
start_stop_step = range(1, 10, 2) # start at 1, stop at 10, count by 2s
# print(up_to_four)


for each_number in up_to_four:
    print(each_number)

for i in start_stop:
    print(i)

sum = 0
for i in start_stop_step:
    sum = sum + i
print(sum)