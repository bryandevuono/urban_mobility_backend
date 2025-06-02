from hash import *
import sys
sys.path.insert(0, '../interface')
import service_engineer
import system_admin
from system_admin import *
import sqlite3

def authenticate_user(username, password):
    #TODO: validate input (required, length format)
    #hard-coded
    if username == "super_admin" and password == "Admin123?":
        return True
    
    #check if username exists and get password and role
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT password, role FROM users
        WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    conn.close()

    #check password
    authenticated = False
    if result:
        authenticated = check_password(result[0], password)
    else:
        print("Username does not exist.")
        return False
    
    # redirect to the correct menu based on role
    if authenticated and result[1] == "service_engineer":
        print("Welcome, service engineer!")
        service_engineer.menu()
        return True
    elif authenticated and result[1] == "system_admin":
        print("Welcome, system administrator!")
        system_admin.menu()
        return True
    else:
        print("Incorrect password.")
        return False