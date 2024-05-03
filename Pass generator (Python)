import random
import string

def generate_password(length=8, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("At least one character type must be included.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
