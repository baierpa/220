# encryption
# for each letter
# 1. get the numerical value
# 2. add our secret key
# 3. decode the new numerical value

sentence = 'the time has come the walrus said'
secret_key = 4
encrypted_sentence = ''
for letter in sentence:
    unicode_value = ord(letter)
    new_number = unicode_value + secret_key
    new_letter = chr(new_number)
    encrypted_sentence = encrypted_sentence + new_letter
print(encrypted_sentence)

# for each letter
# 1. get the numerical value
# 2. subtract our secret key
# 3. decode the new numerical value
encrypted_sentence = 'jvtw|{ly'
secret_key = 7
original_sentence = ''
for letter in encrypted_sentence:
    unicode_value = ord(letter)
    original_number = unicode_value - secret_key
    original_letter = chr(original_number)
    original_sentence = original_sentence + original_letter
print(original_sentence)

# files
# read/write files
my_poem = open('poem.txt', 'r')
# reading files:
#   read() -> returns a string that is the entire file
#   readline() -> returns the next line in the file as a string
#   readlines() -> return all the lines in the file as a list of strings
first_line = my_poem.readline()
next_line = my_poem.readline()
print(first_line, end='')
print(next_line)
my_poem.close()
my_poem = open('poem.txt', 'r')
all_lines = my_poem.readlines()
print(all_lines)
# whole_file = my_poem.read()
# print(whole_file)

# for line in my_poem:
#     print(line, end='')

journal = open('my_journal.txt', 'w')
print("hello, world!", file=journal)
print("how are you?", file=journal)
journal.close()
journal = open('my_journal.txt', 'w')
print('nooooo', file=journal)