# limit = 147
# total = 0
# terms = range(limit)
# for term in terms:
#     total = total + term
# print(total)

first_name = 'joe' # input('enter first name: ')
last_name = 'schmo' # input('enter last name: ')
# two_letters = first_name[0] + first_name[1]
again_two_letters = first_name[0:2]
user_name = last_name + again_two_letters
email = f'{user_name}@g.cofc.edu' # user_name + '@g.cofc.edu'
# print('here is your new email address,', first_name, ':', email)
output = 'here is your new email address, ' + first_name + ': ' + email
easier_output = 'here is your new email address, {0}: {1}'.format(first_name, email)
more_easier_output = f'here is your new email addres, {first_name}: {email}'
print(output)
print(easier_output)

cost = 4/3
cost_output = 'that will cost ${0:.2f}'.format(cost)
another_cost_output = f'that will cost ${cost:.2f}'
print(cost_output)
print(another_cost_output)

# UNICODE
value = ord('a')
character = chr(65)
print(character)

# Encoding - chr -> num
# Decoding - num -> chr
message = 'the time has come the walrus said'
secret_key = 7
for letter in message:
    ordinal = ord(letter) + secret_key
    print(ordinal, end=' ')
print()


numbers = '123 111 108 39 123 112 116 108 39 111 104 122 39 106 118 116 108 39 123 111 108 39 126 104 115 121 124 122 39 122 104 112 107'
number_string_list = numbers.split(' ')
for num_string in number_string_list:
    num_int = eval(num_string) - 7
    letter = chr(num_int)
    print(letter, end='')