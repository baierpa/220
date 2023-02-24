class Car:
    def __init__(self, brand, num_doors):
        self.brand = brand
        self.num_doors = num_doors

    def set_brand(self, brand):
        self.brand = brand

    def set_num_doors(self, num_doors):
        self.num_doors = num_doors

    def get_brand(self):
        return self.brand

    def get_num_doors(self):
        return self.num_doors

class Garage:
    def __init__(self, spaces):
        self.cars = []
        self.spaces = spaces

    def add_car(self, car):
        if self.get_spaces_left() > 0:
            self.cars.append(car)

    def get_car(self, space_number):
        return self.cars[space_number]

    def remove_car(self, car):
        self.cars.remove(car)

    def get_spaces_left(self):
        return self.spaces - len(self.cars)

    def get_total_spaces(self):
        return self.spaces