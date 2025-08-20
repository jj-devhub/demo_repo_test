def is_palindrome(s):
    return s == s[::-1]  # Bug: does not ignore case or spaces

print(is_palindrome("Race car"))
