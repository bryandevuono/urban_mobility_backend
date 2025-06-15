from hash import *
import sys
sys.path.insert(0, './interface')
import service_engineer
import system_admin
import system_admin
import super_admin
import sqlite3
sys.path.insert(0, './encryption')
from symmetric import encrypt_message, decrypt_message

def authenticate_user(username_input, password) -> bool:
    #validate input (required, length format)
    if len(username_input) > 0 and len(password) > 0 and len(username_input) <= 12 and len(password) <= 30:
        pass
    else:
        print("Username and password cannot be empty or too long (12 characters).")
        return False
    
    #hard-coded
    if username_input == "super_admin" and password == "Admin123?":
        super_admin.menu()
        return True
    
    #check if username exists and get password and role
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, id, password, role
        FROM users
    ''')
    users = cursor.fetchall()
    username = ""
    password_db = ""
    role = ""
    for user in users:
        if decrypt_message(user[0]) == username_input:
            username = decrypt_message(user[0])
            password_db = user[2]
            role = user[3]
    conn.close()

    #check password
    authenticated = False
    if username:
        authenticated = check_password(password, password_db)
    else:
        print("Username does not exist.")
        return False
    
    # redirect to the correct menu based on role
    if authenticated and role == "service_engineer":
        service_engineer.menu(username)
        return True
    elif authenticated and role == "system_admin":
        system_admin.menu(username)
        return True
    else:
        print("Incorrect password.")
        return False