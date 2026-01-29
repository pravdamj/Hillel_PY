# Варіант 1
list = [12, 3, 4, 10]
if len(list) <= 1:
    result = list
else:
    result = [list[-1]] + list[:-1]
print(result)

# Варіант 2
list = [1]

if len(list) <= 1:
    result = list
else:
    result = [list[-1]] + list[:-1]
print(result)

# Варіант 3
list = [0]
if len(list) <= 1:
    result = list
else:
    result = [list[-1]] + list[:-1]
print(result)

# Варіант 4
list = [12, 3, 4, 10, 8]
if len(list) <= 1:
    result = list
else:
    result = [list[-1]] + list[:-1]
print(result)