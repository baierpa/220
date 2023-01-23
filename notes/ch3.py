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
print(sum)