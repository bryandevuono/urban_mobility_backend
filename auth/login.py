from hash import *
import sys
sys.path.insert(0, '../interface')
import service_engineer
import system_admin
import system_admin
import super_admin
import sqlite3

def authenticate_user(username, password):
    #TODO: validate input (required, length format)
    #hard-coded
    if username == "super_admin" and password == "Admin123?":
        super_admin.menu()
        return True
    
    #check if username exists and get password and role
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT password, role, username FROM users
        WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    conn.close()

    #check password
    authenticated = False
    if result:
        authenticated = check_password(password ,result[0])
    else:
        print("Username does not exist.")
        return False
    
    # redirect to the correct menu based on role
    if authenticated and result[1] == "service_engineer":
        service_engineer.menu(result[2])
        return True
    elif authenticated and result[1] == "system_admin":
        system_admin.menu(result[2])
        return True
    else:
        print("Incorrect password.")
        return False