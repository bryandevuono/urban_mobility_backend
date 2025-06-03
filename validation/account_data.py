import re

def validate_password(password) -> bool:
    password_re = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)'
    if len(password) > 11 and len(password) < 31 and re.match(password_re, password):
        return True
    else: 
        return False
    
def validate_username(username) -> bool:
    username_re = r"^[a-zA-Z_][a-zA-Z0-9_'.]*$"
    if len(username) > 7 and len(username) < 11 and re.match(username_re, username):
        return True
    else:
        return False