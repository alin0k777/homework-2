test_list = [12, 3, 4, 10, 8]
print(test_list)

if len(test_list) == 0:
    print([])
else:
    last_element = test_list[-1]
    test_list.pop(-1)
    test_list.insert(0, last_element)
    print(test_list)
