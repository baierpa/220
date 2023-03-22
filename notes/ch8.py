# Write a function is_letter(character: string) -> bool, that returns True if the
# given character is a letter, otherwise False
# Test Cases:
#   is_letter()


def is_letter(character):
    # check if it's lowercase or uppercase
    return (character >=  'a' and character <= 'z') or (character >= 'A' and character <= 'Z')

# print(is_letter('a'), "true")
# print(is_letter('z'), "true")
# print(is_letter('A'), "true")
# print(is_letter('Z'), "true")
# print(is_letter('t'), "true")
# print(is_letter('T'), "true")
# print(is_letter('1'), "false")
# print(is_letter('?'), "false")

# Write a function is_upper_case(word: string) -> bool, that returns True if the
# supplied word contains all uppercase letters, otherwise False

def is_upper_case(word):
    for character in word:
        if is_letter(character) and not(character > 'A' and character < 'Z'):
            return False
    return True

print(is_upper_case('hello'), "false")
print(is_upper_case('Hello'), "false")
print(is_upper_case('HELLO'), "true")
print(is_upper_case('HELLO WORLD!'), "true") # Try making this pass!

x = 0
while x < 10:
    print(x)
    x = x + 1
print('done!')
