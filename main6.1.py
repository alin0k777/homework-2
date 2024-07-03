import string

user_input = input("Enter range ex:(a-z): ")
all_letters = string.ascii_letters
first_index = all_letters.index(user_input[0])
second_index = all_letters.index(user_input[len(user_input) - 1])
result = all_letters[first_index:second_index + 1]

print(result)