def avg_for():
    total_numbers_str = input('how many number do you have? ')
    total_numbers = eval(total_numbers_str)
    loop_range = range(total_numbers)
    total = 0
    for i in loop_range:
        user_input = input(f'enter number {i + 1}: ')
        number = eval(user_input)
        total = total + number
    print("the average is", total / total_numbers)

def avg_while():
    i = -1
    total = 0
    user_input = '0'
    while user_input != '':
        number = eval(user_input)
        total = total + number
        i = i + 1
        user_input = input(f'enter number {i + 1} (enter to exit): ')
    print("the average is", total / i)

def file_while():
    file = open('poem.txt', 'r')
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()

def password_check():
    while True:
        password = "helloworld!"
        user_password = input("enter the password: ")
        if user_password == password:
            print("you may enter!")
            break
        else:
            print("incorrect!")
    print("welcome!")

password_check()