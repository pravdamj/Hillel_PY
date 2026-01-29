# Варіант 1
new_list = [12, 3, 4, 10]
if len(new_list) <= 1:
    result = new_list
else:
    result = [new_list[-1]] + new_list[:-1]
print(result)

# Варіант 2
new_list = [1]

if len(new_list) <= 1:
    result = new_list
else:
    result = [new_list[-1]] + new_list[:-1]
print(result)

# Варіант 3
new_list = [0]
if len(new_list) <= 1:
    result = new_list
else:
    result = [new_list[-1]] + new_list[:-1]
print(result)

# Варіант 4
new_list = [12, 3, 4, 10, 8]
if len(new_list) <= 1:
    result = new_list
else:
    result = [new_list[-1]] + new_list[:-1]
print(result)