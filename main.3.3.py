import math

value_list = [1, 2, 3, 4, 5]
list_length = len(value_list)
first_value = math.ceil(list_length / 2)
result_list = [value_list[:first_value], value_list[first_value:]]
print("result list:", result_list)



