a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
action = input("Введіть дію (+, -, *, /): ")

if action == "+":
    result = a + b
    print("Додавання:", result)

elif action == "-":
    result = a - b
    print("Віднімання:", result)

elif action == "*":
    result = a * b
    print("Множення:", result)

elif action == "/":
    if b == 0:
        print("На ноль ділити не можна")
    else:
        result = a / b
        print("Ділення:", result)