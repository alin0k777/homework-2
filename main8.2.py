import string


def is_palindrome(text):
    remove_symb = text.translate(str.maketrans('', '', string.punctuation))
    clean_str = remove_symb.replace(' ', '').lower()
    str_reverse = clean_str[::-1]
    if clean_str == str_reverse:
        return True
    return False


text_test = 'A man, a plan, a canal: Panama'
print('result', is_palindrome(text_test))


