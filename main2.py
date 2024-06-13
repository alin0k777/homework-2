print("please write me a five digit number")
number = input()
print(int(number) % 10,
      int(number) // 10 % 10,
      int(number) // 100 % 10,
      (int(number) // 1000 % 10),
      (int(number) // 10000 % 10), sep='')

