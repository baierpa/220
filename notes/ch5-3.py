sentence = "had" #"the time has come the walrus said"
secret_key = 3
encrypted_sentence = ''
# encryption
# for each letter
#   1. encode letter to number
#   2. add secret key to the number
#   3. decode number to letter
for letter in sentence:
    unicode_value = ord(letter)
    encrypted_value = unicode_value + secret_key
    encrypted_letter = chr(encrypted_value)
    encrypted_sentence = encrypted_sentence + encrypted_letter
print(encrypted_sentence)

# decrypt
secret_key = 3
r = range(1, 27)
for secret_key in r:
    decrypted_sentence = ''
    for letter in encrypted_sentence:
        unicode_value = ord(letter)
        decrypted_value = unicode_value - secret_key
        decrypted_letter = chr(decrypted_value)
        decrypted_sentence = decrypted_sentence + decrypted_letter
    # print(decrypted_sentence)

# files
my_poem = open('poem.txt', 'r')
# read() -> return a string that is the entire file
# readline() -> return a string that is the next line in the file
# readlines() -> return a list of strings that is the entire file

# entire_poem = my_poem.read()
# print(entire_poem.upper())
one_line = my_poem.readline()
next_line = my_poem.readline()
lines_list = my_poem.readlines()

print(one_line)
print(next_line)
print(lines_list)

journal = open('my_journal.txt', 'w')
print("hey", file=journal)
print("sup?", file=journal)

