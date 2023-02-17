# D - Sum all numbers from [1 - 148)
# limit = 147
# total = 0
# terms = range(limit + 1)
# for term in terms:
#     total = total + term
# print(total)

first_name = 'linda' # input('enter first name: ')
last_name = 'bartlett' # input('enter last name: ')
first_two_letters = first_name[:2] # slicing
first_two_letters_again = first_name[0] + first_name[1] # indexing
user_name = last_name + first_two_letters
email = user_name + '@g.cofc.edu'
output = 'hello, ' + first_name + '! Your new email address is: ' + email
output_format = 'hello {0}! Your new email address is: {1}'.format(first_name, email)
output_f_string = f'hello {first_name}! Your new email address is: {email}'
print(output)
print(output_format)
print(output_f_string)

price = 5 / 3
cost = 'that will be ${0:.2f}'.format(price)
cost_f_string = f'that will be ${price:.2f}'
print(cost)
print(cost_f_string)

# 7 -> 0101
# A -> # -> 0110 ?
# Unicode
unicode_value = ord('A')
print(unicode_value)
character = chr(65)
print(character)

sentence = "the time has come the walrus said"
# encoding
for letter in sentence:
    unicode_value = ord(letter) + 7
    print(unicode_value, end=' ')
print()
# decoding
encoded_sentence = '116 104 101 32 116 105 109 101 32 104 97 115 32 99 111 109 101 32 116 104 101 32 119 97 108 114 117 115 32 115 97 105 100'
encoded_list = encoded_sentence.split(' ')
for num in encoded_list:
    letter_number = eval(num)
    character = chr(letter_number)
    print(character, end='')