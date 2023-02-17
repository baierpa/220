# # D - Sum all numbers from [1 - 148)
# limit = 3
# total = 0
# terms = range(limit)
# for term in terms:
#     total = total + term
# print(total)

first_name = 'linda' # input('enter first name: ')
last_name = 'bartlett' # input('enter last name: ')
first_two_letters = first_name[0:2] # slicing
first_two_letters_again = first_name[0] + first_name[1]
r = range(2)
again = ''
for i in r:
    again = again + first_name[i]
user_name = last_name + first_two_letters
print(user_name)
email = user_name + '@g.cofc.edu'
output = 'hello ' + first_name +'. your email address is: ' + email
output_format = 'hello {0}. your email address is: {1}'.format(first_name, 3 + 4 + 5)
output_more_format = f'hello {first_name}. your email address is: {3 + 4 +5}' # f-string
print(output)
print(output_format)
print(output_more_format)

cost = 4/3
cost_output = 'that will be ${0:.2f}'.format(cost)
cost_again_output = f'that will be ${cost:.2f}'
print(cost_output)
print(cost_again_output)

unicode_value = ord('A')
print(unicode_value)
unicode_letter = chr(65)
print(unicode_letter)

# encoding
sentence = 'the time has come the walrus said'
print(sentence)
key = 7 # encryption
for letter in sentence:
    unicode_value = ord(letter) + key
    print(unicode_value, end=' ')
print()
# decoding
encoded_string = '116 104 101 32 116 105 109 101 32 104 97 115 32 99 111 109 101 32 116 104 101 32 119 97 108 114 117 115 32 115 97 105 100'
encoded_list = encoded_string.split()
for num in encoded_list:
    num_int = eval(num) - key
    character = chr(num_int)
    print(character, end='')

