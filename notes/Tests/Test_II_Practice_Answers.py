# Required
sentence = "Intelligence is the ability to avoid doing work, yet getting the work done."
output_list = []
for character in sentence:
    output_list.append(character)
print(output_list)

# A
from Parking import Car, Garage

toyota = Car("Toyota", 4)
honda = Car("Honda", 2)
garage = Garage(3)
garage.add_car(honda)
garage.add_car(toyota)
first_car = garage.get_car(1)
first_car_brand = first_car.get_brand()
first_car_doors = first_car.get_num_doors()
print(first_car_brand, first_car_doors)
garage.remove_car(honda)
spaces_left = garage.get_spaces_left()
print(spaces_left)
total_spaces = garage.get_total_spaces()
print(total_spaces)

# B
from graphics import Point, Polygon

star = Polygon(Point(2, 1), Point(5, 3),
               Point(8, 1), Point(7, 4),
               Point(9, 6), Point(6, 6),
               Point(5, 9), Point(4, 6),
               Point(1, 6), Point(3, 4))
star.setWidth(3)

# C
sentence = "communities agree on a disputer"
first_three = sentence[:3]
last_five = sentence[-5:]
fold = first_three + last_five
print(fold)

# D
middle_search = ['And', 'all', 'the', 'people', 'that', 'come', 'and', 'go']
middle_index = len(middle_search) // 2
middle_item = middle_search[middle_index]
print(middle_item)

# Plus
number_string = "314159265359"
total = 0
for number in number_string:
    num = eval(number)
    total = total + num
print(total)