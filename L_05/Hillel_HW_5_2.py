while True:
    a = float(input("Введіть перше число: "))
    action = input("Введіть дію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))


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
    else:
        print("Невідома дія")

    next = input("Продовжити роботу? (yes/y): ").lower()
    if next not in ("yes", "y"):
        print("Роботу завершено")
        break
