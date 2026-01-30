import re

def validate(password):
    result = {
        'length': len(password) > 7,
        'has_digit': bool(re.search(r'[0-9]', password)),
        'has_special': any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password),
        'has_uppercase': bool(re.search(r'[A-Z]', password)),
        'has_lowercase': bool(re.search(r'[a-z]', password)),
        'has_letter': False,
    }
    result['has_letter'] = result['has_uppercase'] or result['has_lowercase']
    for i in result.values():
        if not i:
            return (False, result)
    return (True, result)

is_valid, errors = validate(input())
while not is_valid:
    for error, is_not_error in errors.items():
        if not is_not_error:
            print(error)
    is_valid, errors = validate(input('Try again: '))