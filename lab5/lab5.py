import re


# 1️⃣ Match a string that has an 'a' followed by zero or more 'b's.
def check_pattern(string, pattern):
    for s in string:
        if re.fullmatch(pattern, s):
            print(f'1:{s} yes match')
        else:
            print(f'1:{s} no match')


pattern = r'ab*'
string = ["ab", "abb", "ac"]
check_pattern(string, pattern)


# 2️⃣ Match a string that has an 'a' followed by two to three 'b's.
def check_pattern(string, pattern):
    for s in string:
        if re.fullmatch(pattern, s):
            print(f'2:{s} yes match')
        else:
            print(f'2:{s} no match')


pattern = r'ab{2,3}'
string = ["ab", "abb", "ac"]
check_pattern(string, pattern)

# 3️⃣ Find sequences of lowercase letters joined with an underscore.
text3 = "hello_world test_text abc_123"
pattern3 = r'[a-z]+_[a-z]+'
print("3:", re.findall(pattern3, text3))

# 4️⃣ Find sequences of one uppercase letter followed by lowercase letters.
text4 = "Hello there, My name is Birzhan"
pattern4 = r'[A-Z][a-z]+'
print("4:", re.findall(pattern4, text4))


# 5️⃣ Match a string that has an 'a' followed by anything, ending in 'b'.
def check_pattern(string, pattern):
    for s in string:
        if re.fullmatch(pattern, s):
            print(f'{s} yes match')
        else:
            print(f'{s} not match')


pattern = r'a.*b$'
string = ["abb", "aeeeeb", "ahhhb"]
check_pattern(string, pattern)

# 6️⃣ Replace all occurrences of space, comma, or dot with a colon.
text6 = "Python, regex is fun. Let's learn more"
pattern6 = r"[ ,.]"
result6 = re.sub(pattern6, ":", text6)
print("6:", result6)

# 7️⃣ Convert snake_case string to camelCase string.
text7 = "hello_world_python"


def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


print("7:", snake_to_camel(text7))

# 8️⃣ Split a string at uppercase letters.
text8 = "SplitThisStringAtUppercase"
result8 = re.split(r'(?=[A-Z])', text8)
print("8:", result8)

# 9️⃣ Insert spaces between words starting with capital letters.
text9 = "InsertSpaceBetweenWords"
result9 = re.sub(r'(?=[A-Z])', ' ', text9).strip()
print("9:", result9)

# 🔟 Convert a given camelCase string to snake_case.
text10 = "convertThisStringToSnakeCase"
result10 = re.sub(r'(?<!^)(?=[A-Z])', '_', text10).lower()
print("10:", result10)