from graphics import Point
# strings, lists, files
# Constructor, instance variables, methods
greeting = 'hello WORLD!' # str
p = Point(3, 5)

# immutability vs mutability
# string are immutable!
lower_greeting = greeting.lower()
# print(greeting, lower_greeting)

# points are mutable!
p.move(10, 0)
# print(p.getX())

upper_greeting = greeting.upper()
# print(upper_greeting, greeting)

capital_greet = greeting.capitalize()
# print(capital_greet)

title_greet = greeting.title()
# print(title_greet)

greeting = 'hello, WORLD!'
l_count = greeting.count('hello')
# print(l_count)

# find/rfind
l_index = greeting.rfind('WORLD')
# print(l_index)

new_greeting = greeting.replace(' ', '')
# print(new_greeting)

name = '    Jamie    '
print(name.strip(), name.rstrip(), name.lstrip())

name = 'Jamie'
print(name.center(11, '*'), name.ljust(11, '^'), name.rjust(11, '$'))

name_length = len(name)
print(name_length)

# string operators + Concatenation, * Repetition
first_name = 'pat'
last_name = 'smith'
full_name = first_name + ' ' + last_name
print((full_name + ' ') * 5)

# indexing
# []
third_letter = full_name[2]
print(third_letter)

# Lists - Sequence of elements/objects
#Constructor, Instance Variable, Methods
my_numbers = [100, 200, 300, 400]
first_number = my_numbers[0]
print(first_number)
my_numbers.append(500)
print(my_numbers)

for i in my_numbers:
    pass
for letter in name:
    pass