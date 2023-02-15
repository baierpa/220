from graphics import Point
# String, Lists, Files
# Constructor, Instance Variables, Methods

greeting = 'hello, WORLD!' # str

p = Point(3, 4)

# mutability / immutability
# string are immutable!
lower_greeting = greeting.lower()
# print(lower_greeting, greeting)

# Points are mutable!
p.move(10, 0)
# print(p.getX())

upper_greeting = greeting.upper()
# print(upper_greeting)

greeting_capital = greeting.capitalize()
# print(greeting_capital)

greeting_title = greeting.title()
# print(greeting_title)

greeting = "hello, WORLD!"
occurances = greeting.count("l")
# print(occurances)

# index values - position of letter in string
# find/rfind
position = greeting.rfind("x")
# print(position)

new_greeting = greeting.replace(" ", "")
print(new_greeting)

name = "    Jamie Johns     "
# print(name.strip(), name.rstrip(), name.lstrip())

name = "Sally Sam"
# print(name.center(19, '*'), name.rjust(19, '#'), name.ljust(19, '$'))

# operators + concatenation, * repetition
first_name = 'billy'
last_name = 'joel'
full_name = first_name + ' ' + last_name
# print(full_name * 5)

name_length = len(full_name)
print(name_length)

# indexing
first_letter = full_name[0]
print(first_letter)

# lists
# constructor
my_numbers = [100, 200, 300, 400]
first_number = my_numbers[0]
my_numbers.append(500)
print(my_numbers)

for num in my_numbers:
    print(num)
for letter in full_name:
    print(letter)