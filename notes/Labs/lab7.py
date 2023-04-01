'''
should know:
    reading/writing files
    lists
    string methods
    basic conditionals
'''


def weighted_average(in_file_name, out_file_name):
    # open input and output files
    file_input = open(in_file_name, 'r')
    file_output = open(out_file_name, "w")
    class_totals = []
    # loop through each line in the input file
    for student in file_input:
        entry = student.split(':')
        name = entry[0]
        numbers = entry[1].strip().split(' ') # creates a list of strings that are numbers
        weights = numbers[::2] # get every other value starting at 0
        grades = numbers[1::2] # get every other value starting at 1
        # go through each weight/grade combo, summing the weights and average
        total = 0
        weight_total = 0
        total_grades = range(len(grades))
        for i in total_grades:
            weight = eval(weights[i]) # get weight value and convert to integer
            grade = eval(grades[i]) # get grade value and convert to integer
            weight_total = weight_total + weight
            total = total + (weight * grade)

        # handle output based on the weight total
        if weight_total == 100:
            rounded_total = round(total/100, 1)
            print(f"{name}'s average: {rounded_total}", file=file_output)
            class_totals.append(rounded_total)
        elif weight_total < 100:
            print(f"{name}'s average: Error: The weights are less than 100.", file=file_output)
        else:
            print(f"{name}'s average: Error: The weights are more than 100.", file=file_output)

    # calculate the class average
    class_total = 0
    for total in class_totals:
        class_total = class_total + total
    class_average = round(class_total/len(class_totals), 1)
    print(f'Class average: {class_average}', file=file_output)

weighted_average('grades.txt', 'avg.txt')
