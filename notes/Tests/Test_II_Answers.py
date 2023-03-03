from graphics import Point, Line, Oval
from Travel import Passenger, Ticket

# A - Use the Passenger and Ticket class

passenger = Passenger("Michael", "Corleone", 37)
ticket = Ticket("NYC", "Vegas", 323, passenger)
ticket.assign_seat('20A')
ticket.set_arrival('CHS')
passenger.set_frequent_flier_number(1234)

# B - Recreate the image

# Option I
p1 = Point(4,4)
p2 = Point(7, 7)
line = Line(p1, p2)
line.setArrow("last")

oval = Oval(Point(6, 6), Point(8, 8))
oval2 = Oval(Point(3, 6), Point(5, 2))

# Option II
line = Line(Point(3, 5), Point(7, 5))
line.setArrow('both')

left = Oval(Point(4, 7), Point(6, 8))
right = Oval(Point(3, 7), Point(7, 3))

# Option III
line1 = Line(Point(3, 4), Point(5, 8))
line1.setArrow("first")

line2 = Line(Point(7, 4), Point(5, 8))
line2.setArrow("first")

oval = Oval(Point(2, 3), Point(8, 5))

# C - Print the first letter of each word in "a sweet part goes a wonderful life"
sentence = "a sweet part goes a wonderful life"
words = sentence.split()
for word in words:
    print(word[0], end='')

print()
# D - Print "the happy fish thinks a new work" with the letter 'a' after each character
sentence = "the happy fish thinks a new work"
for character in sentence:
    print(character, end='')
    print('a', end='')

print()
# Plus - What is the sum of the unicode values of each character in "a new penguin makes the pretty penguin"
sentence = "a new penguin makes the pretty penguin"
total = 0
for character in sentence:
    total = total + ord(character)
print(total)

# Required - Create a list where each element is an uppercase word from "a great company tries the good hand" followed by 'yay'.
sentence = "a great company tries the good hand"
words = sentence.split()
output = []
for word in words:
    output.append(word.upper())
    output.append("yay")
print(output)
