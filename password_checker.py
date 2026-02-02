import re

def password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_error = re.search(r"[@#$%!&]", password) is None

    errors = sum([
        length_error,
        uppercase_error,
        lowercase_error,
        digit_error,
        special_error
    ])

    if errors == 0:
        return "Strong Password "
    elif errors <= 2:
        return "Medium Password "
    else:
        return "Weak Password "

# User input
pwd = input("Enter your password: ")
print(password_strength(pwd))
