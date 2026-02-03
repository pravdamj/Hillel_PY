first_list = [1, 0, 13, 0, 0, 0, 5]
new_list = []

for el in first_list:
    if el != 0:
        new_list.append(el)

for el in first_list:
    if el == 0:
        new_list.append(0)

print(new_list)

