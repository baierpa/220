name = "Philip"
people = ["jane", "john", "jim", name]
#
# print(people)
# # people = people + ["jack"]
# people.append("jack")
# print(people)
#
# # + *
# last_name = "Mickleson"
# full_name = name + " " + last_name
# print(full_name * 5)
# people = people + ["sally", "sammy"]
# # print(people)
# people = ['jake'] + people
# print(people * 2)
#
# print(len(name), len(people))

print(name[0], people[2])
# letter = name[0], letter = name[1], letter = name[2], ...
for letter in name:
    print(letter, end=' ')
print()
# person = people[0], person = people[1], ...
# for person in people:
#     print(person, end=' ')
# print()
name_range = range(len(name))
# for i in name_range:
#     letter = name[i]
#     print(letter, end=' ')

sentence = "The time has come the walrus said"
words = sentence.split()
print(words)

joined_list = ' '.join(words)
print(joined_list)

days = 'montuewedthufrisat'
print(days[0], days[ len(days) - 1 ])
print(days[-1], days[len(days) * -1])

# slicing
# [start:stop:step]
day = days[::-1]
print(day, words[1:4])

num_string = str(1234567)
