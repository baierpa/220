name = "Philip"
participants = ["Steve", "Joe", "Jane", "Linda", name]
print(participants)
participants.append("Sam")
participants.append("Pat")
print(participants)

# print(len(name), len(participants))

# print(name[0], participants[0])
participant_b = participants[3]
# print(participant_b[ len(participant_b) * -1 ]) # first letter/element [0]
# print(participant_b[-1]) # last letter/element [ len(participant_b) - 1 ]

days = 'montuewedthufrisatsun'
nums = [45, 46, 47]
print(days[3])
# slicing [start:stop:step]
print(days[3:], nums[:2], nums[::-1])
backwards = nums[::-1]
print(nums, backwards)

# + *
name = "Philip"
last_name = "Phillips"
nums = [45, 46, 47]

full_name = name + " " + last_name
# print(full_name * 5)
nums.append(48)
nums = nums + [49, 50, 51, 52]
# print(nums * 5)

num = 123456789
num_string = str(num)

sentence = "the time has come the walrus said"
words = sentence.split()
print(words)
joined = ' '.join(words)
print(joined)