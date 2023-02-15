name = "Philip"
ages = [30, 41, 82, 22]

# print(len(name), len(ages))
# + *
full_name = "laura" + " " + "croft"
more_ages = ages + [44, 55, 66]
# print(full_name * 5, more_ages * 2)

names = ['janie', 'jamie', 'johnny', name]
name1 = names[0]
# print(name[0], ages[0], names[0])

# letter = name[0], letter = name[1], letter=name[2], ...
# for letter in name:
#     print(letter, end=' ')
# print()
#
# for name in names:
#     print(name, end=' ')
# print(names)
names = names + ['ralph']
# names.append('ralph')
# print(names)

num = str(123456789)
# print()
sentence = "the time has come the walrus said"
words = sentence.split(' ')
print(words)
split_num = num.split('5')
print(split_num)

joined_string = '-'.join(words)
print(joined_string)

days = 'montuewedthufrisatsun'
print(days[ len(days) - 1 ]) # last letter days[-1]
print(days[-1 * len(days)]) # first letter days[0]
# slicing
# [start : stop : step]
tuesday = days[3:6]
# print(tuesday)

names = ['janie', 'jamie', 'johnny', name]
jamie_and_johnny = names[1:3]
# print(jamie_and_johnny)

# print(names[1:], names[:2])
print(names[3:1:-1], days[::-1])