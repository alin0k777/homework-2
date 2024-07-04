def multiple_digit(digit):
    if digit <= 9:
        return digit

    result = 1
    for n in str(digit):
        result *= int(n)

    return multiple_digit(result)


user_input = input("Enter number: ")
print('result', multiple_digit(int(user_input)))


