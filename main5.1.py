import keyword
import string


def is_valid_variable_name(word):

    if word[0].isdigit():
        return False

    for el in word:
        if el.isupper():
            return False

        if el in string.punctuation.replace('_', ''):
            return False

    if word in keyword.kwlist:
        return False

    if word.count('_') > 1:
        parts = word.split('_')
        for part in parts:
            if not part:
                return False

    return True


user_input = input("Enter word: ")
print(is_valid_variable_name(user_input))
