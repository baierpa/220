# Write a function is_letter(character: string) -> bool, that returns True if the
# given character is a letter, otherwise False

# Test Cases

def is_letter(character):
    return (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')

# print(is_letter('a'), "true")
# print(is_letter('A'), "true")
# print(is_letter('z'), "true")
# print(is_letter('Z'), "true")
# print(is_letter('b'), "true")
# print(is_letter('B'), "true")
# print(is_letter('1'), "false")
# print(is_letter('!'), "false")

# Write a function is_upper_case(word: string) -> bool, that returns True if the
# supplied word contains all uppercase letters, otherwise False

def is_upper_case(word):
    for character in word:
        if is_letter(character) and not(character >= 'A' and character <= 'Z'):
            return False
    return True

# test cases
print(is_upper_case("ANYTHING"), "true")
print(is_upper_case("Anything"), "false")
print(is_upper_case("anything"), "false")
print(is_upper_case("1234567890"), "false")
print(is_upper_case("!!!!"), "false")
print(is_upper_case("HELLO WORLD!"), "true")

x = 0
while x < 10:
    print(x)
    x = x + 1
print('done!')


