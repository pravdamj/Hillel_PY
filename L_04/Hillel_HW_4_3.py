import random
numbers = random.randint(3, 10)
first_list = [random.randint(3, 10) for el in range(numbers)]
second_list = first_list[0], first_list[2], first_list[-2]
print(second_list)

