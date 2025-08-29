import re

def validate_email(email):
    # Bug fixed: proper email validation with regex
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    # Bug fixed: check that all characters are digits
    if len(phone) == 10 and phone.isdigit():
        return True
    return False

def validate_password(password):
    # Bug fixed: check for uppercase, numbers, and special characters
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    return has_upper and has_digit and has_special

# Test cases that should fail but will pass with buggy validation
print(f"Email 'user@' is valid: {validate_email('user@')}")
print(f"Phone 'abcdefghij' is valid: {validate_phone('abcdefghij')}")
print(f"Password 'password' is valid: {validate_password('password')}")
