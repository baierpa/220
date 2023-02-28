roads_input = input('How many roads were surveyed? ')
roads = eval(roads_input)

running_total_cars = 0
running_total_days = 0

road_range = range(roads)
for road in road_range:
    print('How many days was road', road + 1, 'surveyed?: ', end='')
    days_input = input()
    days = eval(days_input)
    running_total_days = running_total_days + days
    spot_total_cars = 0
    days_range = range(days)
    for day in days_range:
        print('\tOn day', day + 1, 'how many cars traveled? ', end='')
        cars_input = input()
        cars = eval(cars_input)
        spot_total_cars = spot_total_cars + cars
        running_total_cars = running_total_cars + cars
    average = spot_total_cars / days
    rounded_average = round(average, 2)
    print('Road', road + 1, 'average vehicles per day: ', rounded_average)

print('Total number of vehicles travelled on all roads: ', running_total_cars)
average_per_road = running_total_cars / roads
rounded_average_per_road = round(average_per_road, 2)
print(f'Average number of vehicles per road: ', rounded_average_per_road)
