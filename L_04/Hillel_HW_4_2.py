first_list = [0, 1, 7, 2, 4, 8]
result = []

for el in range(0, len(first_list), 2):
    result.append(first_list[el])

sum_result = sum(result)
print(sum_result * (first_list[-1]))





