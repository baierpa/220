def for_average():
    total_nums_string = input("how many numbers do you have? ")
    total_nums = eval(total_nums_string)
    loop_range = range(total_nums)
    total = 0
    for i in loop_range:
        number_string = input("enter a number: ")
        number = eval(number_string)
        total = total + number
    print('the average is: ', total / total_nums)


def while_average():
    iterations = 0
    total = 0
    number_string = input("enter a number (enter to quit): ")
    while number_string != '':
        number = eval(number_string)
        total = total + number
        iterations = iterations + 1
        number_string = input("enter a number (enter to quit): ")
    print('the average is: ', total / iterations)


def file_loop():
    file = open('poem.txt', 'r')
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()
    file.close()

def password_check():
    password = 'helloworld!'
    while True:
        user_guess = input("enter the password: ")
        if user_guess == password:
            print('you may enter!')
            break
        else:
            print('incorrect! try again')

password_check()
