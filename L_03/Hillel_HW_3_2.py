list = [12, 3, 4, 10]

if len(list) <= 1:
    result = list
else:
    result = [list[-1]] + list[:-1]

print(result)