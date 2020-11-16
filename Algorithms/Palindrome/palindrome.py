def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(f"Is 'Mother' a palindrome? {is_palindrome('Mother')}")
print(f"Is 'Mom' a palindrome? {is_palindrome('Mom')}")
