import os
import sys

sys.path.insert(0, '../auth')

from login import authenticate_user 

clear = lambda: os.system('clear')

def welcome_screen():
    print("Welcome to the urban mobility system\n"
           "Choose an option:\n"
           "\nLogin (enter L)\n"
           "Register (enter R)")
    login_option = input()

    if (login_option.lower() == "l" and len(login_option) < 2):
        clear()
        login_screen()
    else:
        print("Wrong key, please try again")

def login_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        login_attempt = authenticate_user(username, password)
        if login_attempt:
            print("logged in")
            break
        else:
            continue
            
def signup_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        firstname = input("Enter your password\n")
        lastname = input("Enter your password\n")
welcome_screen()