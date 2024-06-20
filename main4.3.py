import random

list_range = random.randint(3,10)
list_test = []
list_result = []
count = 0
while count < list_range:
    list_test.append(random.randint(1,10))
    count += 1

print(list_test)

list_result.append(list_test[0])
list_result.append(list_test[2])
list_result.append(list_test[len(list_test) - 2])

print(list_result)
