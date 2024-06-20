test_list = [0, 1, 0, 12, 3, 0, 0, 4, 2, 6]
result_list = []
for element in test_list:
    if element != 0:
        result_list.append(element)

while len(test_list) != len(result_list):
    result_list.append(0)

print(result_list)