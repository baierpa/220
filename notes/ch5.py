from graphics import Point
# Strings, Lists, Files
# Constructor, Instance Variables, Methods
greeting = 'hello, WORLD!'
lower_greeting = greeting.lower()
# mutability/immutability - can it change?
# strings are immutable
# print(greeting, lower_greeting)
# Points are mutable
p = Point(3, 4)
p.move(1, 0)
# print(p.getX())
upper_greeting = greeting.upper()
# print(upper_greeting)
greeting.capitalize()
greeting.title()
l_count = greeting.count('el')

greeting = 'hello, world!'
el_location = greeting.find('l')
el_location = greeting.rfind('l')
# print(el_location)
# index - position of letter within the string starting at 0

greeting = 'hello, world! how are you?'
no_spaces = greeting.replace('', ' ')
# print(no_spaces, greeting)

# center, ljust, rjust
name = '   Patty   '
# print(name.center(11, '*'), name.ljust(11, '$'), name.rjust(11, 'h'))

# lstrip, rstrip, strip- takes out space before/after the string object

# Operators + *
# + concatenation
first_name = 'george'
last_name = 'baily'
full_name = first_name + ' ' + last_name
# print(full_name)
# * repetition
repeat = (first_name + ' ') * 5

name = 'jane'
last_letter = name[3] # indexing
print(last_letter)

x = range(19)
for letter in name:
    print(letter)

# Lists
my_numbers = [100, 509, 300, 400]
# indexing
second_element = my_numbers[1]
print(second_element)
for number in my_numbers:
    print(number)

my_numbers.append(1000)
print(my_numbers)
