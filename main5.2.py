while True:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    what = input("Выберите действие, могу предложить: +, -, *, /")

    if what == "+":
        print("Результат:", first + second)
    elif what == "-":
        print("Результат:", first - second)
    elif what == "*":
        print("Результат:", first * second)
    elif what == "/":
        if second != 0:
            print("Результат:", first / second)
        else:
            print("Делить на ноль нельзя")
    else:
        print("Неверное действие")

    continue_calculating = input("Хотите продолжить? (yes/no для продолжения): ")
    if continue_calculating.lower() not in ["yes", "y"]:
        break

print("Работа калькулятора завершена")
