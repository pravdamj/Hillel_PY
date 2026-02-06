import string
string_letters = input('Please enter letter ')
first, last = string_letters.split('-')
result = ""
for el in string.ascii_letters:
    if first <= el <= last:
        result += el
print(result)

