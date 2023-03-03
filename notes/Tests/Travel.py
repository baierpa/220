"""
Passenger

Constructor
Passenger(first_name: str, last_name: str, age: int)
Constructs a Passenger with the given first name, last name, and age

Methods
get_name() -> str
Returns the passenger’s name in the format last_name, first_name

set_frequent_flier_number(ffn: int) -> None
Sets the passenger’s frequent flier number

"""

"""
Ticket

Constructor
Ticket(dep: str, arr: str, flight_num: int, passenger: Passenger)
Constructs a plane ticket with a departure city (where the plane leaves from), arrival city (where the plane lands), flight number, and the passenger to whom the ticket belongs.

Methods
assign_seat(seat_assignment: str) -> None
Sets the ticket’s seat assignment. Seat assignments are strings that contain the seat number (any number from 1-100) and a single letter representing the seat position  (letters are from A - J). ex: ‘27B’

set_departure(new_city: str) -> None
Sets the ticket’s departure city to new_city

set_arrival(new_city: str) -> None
Sets the ticket’s arrival city to new_city
"""


class Ticket:

    def __init__(self, dep, arr, flight_num, passenger):
        self.seat_assignment = None
        if not type(passenger) == Passenger:
            raise TypeError('passenger must be a Passenger object')
        self.dep = dep
        if not type(dep) == str:
            raise TypeError('departure must be a str object')
        self.arr = arr
        if not type(arr) == str:
            raise TypeError('arrival must be a str object')
        self.flight_num = flight_num
        if not type(flight_num) == int:
            raise TypeError('flight_num must be an int')
        self.passenger = passenger

    def assign_seat(self, seat_assignment):
        try:
            letter = seat_assignment[-1].upper()
            seat_number = int(seat_assignment[:-1])
            letter_ord = ord(letter)
            self.seat_assignment = seat_assignment
        except ValueError:
            raise ValueError('invalid seat number. check seat assignment format')
        except TypeError:
            raise TypeError('invalid seat letter. check seat assignment format')
        except:
            print('invalid seat assignment. check seat assignment format')

    def set_departure(self, new_city):
        self.dep = new_city
        if not type(new_city) == str:
            raise TypeError('departure must be a str object')

    def set_arrival(self, new_city):
        self.arr = new_city
        if not type(new_city) == str:
            raise TypeError('arrival must be a str object')


class Passenger:

    def __init__(self, first_name, last_name, age):
        self.ffn = None
        self.first_name = first_name
        if not type(first_name) == str:
            raise TypeError(f'first_name expected a str but {type(first_name)} found')
        self.last_name = last_name
        if not type(last_name) == str:
            raise TypeError(f'last_name expected a str but {type(last_name)} found')
        self.age = age
        if not type(age) == int:
            raise TypeError(f'age expected an int but {type(age)} found')

    def get_name(self):
        return f'{self.last_name}, {self.first_name}'

    def set_frequent_flier_number(self, ffn):
        if not type(ffn) == int:
            raise TypeError(f'set_frequent_flier_number() expected an int but {type(ffn)} found')
        self.ffn = ffn