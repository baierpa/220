def average_for():
    total_numbers_str = input('how many numbers will we add? ')
    total_numbers = eval(total_numbers_str)
    loop_range = range(total_numbers)
    total = 0
    for i in loop_range:
        number_input = input(f'enter number {i + 1}: ')
        number = eval(number_input)
        total = total + number
    print('the average is: ', total / total_numbers)

def average_while():
    i = 0
    total = 0
    number_input = input(f'enter number {i + 1} (enter to quit): ')
    while number_input != '':
        number = eval(number_input)
        total = total + number
        i = i + 1
        number_input = input(f'enter number {i + 1} (enter to quit): ')
    print('the average is: ', total / i)

def file_while():
    file = open('poem.txt', 'r')
    line = file.readline()
    while line != '':
        line = file.readline()
        print(line, end='')

# file_while()

def password_check():
    while True:
        password = 'helloworld!'
        user_password = input("enter password: ")
        if user_password == password:
            print('you may enter!')
            break
        else:
            print('incorrect!')
    print('goodbye')

# password_check()

r = range(100)
for i in r:
    if i > 50:
        break
    print(i)