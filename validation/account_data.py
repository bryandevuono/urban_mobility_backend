import re

def validate_password(password) -> bool:
    password_re = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'
    if len(password) > 11 and len(password) < 31 and re.match(password_re, password):
        return True
    else: 
        print("Password must be between 12 and 30 characters long, contain at least one digit, one lowercase letter, one uppercase letter, and one special character.")
        return False
    
def validate_username(username) -> bool:
    username_re = r"^[a-zA-Z_][a-zA-Z0-9_'.]*$"
    if len(username) > 7 and len(username) < 11 and re.match(username_re, username):
        return True
    else:
        print("Username must be between 8 and 10 characters long, start with a letter or underscore, and contain only alphanumeric characters, underscores, apostrophes, or periods.")
        return False
    
def validate_name(name):
    if len(name) > 0 and len(name) < 36 and name.isalpha():
        return True
    else:
        print("Name must be between 1 and 35 characters long. Use only alphabetic characters.")
        return False