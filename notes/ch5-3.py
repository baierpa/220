def encrypt():
    message = 'the time has come the walrus said'
    secret_key = 4
    encoded = []
    encrypted = []
    encrypted_string = ''
    for letter in message:
        letter_value = ord(letter)
        encoded.append(letter_value)
        new_letter_value = letter_value + secret_key
        encrypted.append(new_letter_value)
        new_letter = chr(new_letter_value)
        encrypted_string = encrypted_string + new_letter
    print(encoded)
    print(encrypted)
    print(encrypted_string)

def decrypt():
    encrypted_string = "xli$xmqi$lew$gsqi$xli${epvyw$wemh"
    secret_key = 4
    original_string = ''
    for letter in encrypted_string:
        # get the numeric value
        letter_value = ord(letter)
        # subtract key value
        original_value = letter_value - secret_key
        # convert back to letter
        original_letter = chr(original_value)
        original_string = original_string + original_letter
    print(original_string)

# encrypt()
# decrypt()

# files
#  need to be opened / closed
my_poem_file = open('poem.txt', 'r')
# my_poem_file.read()
#   return the entire file as a string
# my_poem_file.readline()
#   return the next line from the file
line_one = my_poem_file.readline()
another_line = my_poem_file.readline()
print(line_one)
print(another_line)
# my_poem_file.readlines()
#   return all the lines of the file in a list of strings
all_lines_list = my_poem_file.readlines()
print(all_lines_list)

my_poem_file.close()
my_poem_file = open('poem.txt', 'r')
# all_file = my_poem_file.read()
# print(all_file)
for line in my_poem_file:
    words = line.split()
    print(words)

my_poem_file.close()

my_writing_file = open('journal.txt', 'w')
print('hello, world!', file=my_writing_file)
print('how are you?', file=my_writing_file)
my_writing_file.close()
