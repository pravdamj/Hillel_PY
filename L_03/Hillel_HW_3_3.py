first_list = [2, 4, 7, 11, 0, 2, 8]
size = len(first_list)
print(size)

if size == 0:
    result = [[], []]
else:
    middle = size // 2
    if size % 2 != 0:
         middle = middle + 1
    result = [[], []]
    result[0] = first_list[:middle]
    result[1] = first_list[middle:]

print(result)
