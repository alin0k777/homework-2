# Реализация elif

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
what = input("Выберите действие, могу предложить: +, -, *, /,")
# if what == "+":
#     print(first + second)
# elif what == "-":
#     print(first - second)
# elif what == "*":
#     print(first * second)
# elif what == "/":
#    if second != 0:
#        print(first / second)
#    else:
#        print("Делить на ноль нельзя")


# Реализация через match

match what:
    case "+":
        print(first + second)
    case "-":
        print(first - second)
    case "*":
        print(first * second)
    case "/":
        if second != 0:
            print(first / second)
        else:
            print("Делить на ноль нельзя")
