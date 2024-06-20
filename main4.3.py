test_list = [0, 1, 7, 2, 4, 8, 9, 3, 10]
index = 0
summ = 0

for el in test_list:
    index = index + 1
    if index % 2 == 0:
        summ = summ + el

print('sum', summ)
print(summ * test_list[len(test_list) - 1])
