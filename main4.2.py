test_list = [0, 1, 7, 2, 4, 8, 9, 3, 10]
index = 0
summ = 0

for el in test_list:
    if index % 2 == 0:
        summ = summ + el
    index = index + 1

print(summ * test_list[len(test_list) - 1]) if len(test_list) else print(0)

