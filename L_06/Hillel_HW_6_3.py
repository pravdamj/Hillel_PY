number = int(input('Please enter number '))

while number > 9:
    result = 1
    for el in str(number):
        result = result * int(el)
    number = result

print(number)
