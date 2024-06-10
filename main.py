print("please write me a four digit number")
number = input()

# first variant
# print(number[0] + '\n')
# print(number[1] + '\n')
# print(number[2] + '\n')
# print(number[3] + '\n')

# second variant
print(int(number) // 1000)
print(int(number) // 100 % 10)
print(int(number) // 10 % 10)
print(int(number) % 10)