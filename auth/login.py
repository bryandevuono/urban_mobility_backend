import sqlite3
def authenticate_user(username, password):
    #validate input (required, length format)
    #hard-coded
    if username == "super_admin" and password == "Admin123?":
        return True
    #check if username exists

    #check password