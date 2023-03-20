# Write a function is_letter(character: string) -> bool, that returns True if the
# given character is a letter, otherwise False

# Test Cases:
#   print(is_letter('a')) -> True
#   print(is_letter('2')) -> False
#   print(is_letter('A')) -> True
#   print(is_letter(' ')) -> False
#   print(is_letter('z')) -> True
#   print(is_letter('Z')) -> True
#   print(is_letter('h')) -> True
#   print(is_letter('H')) -> True
#   print(is_letter('!')) -> False

def is_letter(character):
    return (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')

# print(is_letter('a'), "true")
# print(is_letter('2'), "false")
# print(is_letter('A'), "true")
# print(is_letter(' '), "false")
# print(is_letter('z'), "true")
# print(is_letter('Z'), "true")
# print(is_letter('h'), "true")
# print(is_letter('H'), "true")
# print(is_letter('!'), "false")

# Write a function is_upper_case(word: string) -> bool, that returns True if the
# supplied word contains all uppercase letters, otherwise False

# print(is_upper_case('hello'), 'false')
# print(is_upper_case('HELLO'), 'true')

def is_upper_case(word):
    for character in word:
        if is_letter(character) and not(character >= 'A' and character <= 'Z'):
        # if not(character >= 'A') or not(character <= 'Z'):
            return False
    return True

print(is_upper_case('hello'), 'false')
print(is_upper_case('HELLO'), 'true')
print(is_upper_case('Hello'), 'false')
print(is_upper_case('HELLO WORLD!'), 'true') # make this work!


x = 0
while x < 10:
    print(x)
    x = x + 1
print('done!')


