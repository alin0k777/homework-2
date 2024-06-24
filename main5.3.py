my_string = 'Should, I. subscribe? Yes!'

pre_result = my_string.title()
result = "#" + (''.join(char for char in pre_result if char.isalnum()))
print(result)