import os
import sys
from super_admin import menu as super_admin_menu
sys.path.insert(0, '../auth')

from login import authenticate_user 

clear = lambda: os.system('cls')

def welcome_screen():
    while True:
        print("Welcome to the urban mobility system\n"
           "Choose an option:\n"
           "\nLogin (enter L)\n"
           "Register (enter R)")
        login_option = input()
        if (login_option.lower() == "l" and len(login_option) < 2):
            clear()
            login_screen()
            break
        if (login_option.lower() == "r" and len(login_option) < 2):
            clear()
            signup_screen()
            break
        else:
            clear()
            print("Wrong key, please try again")
            continue

def login_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        login_attempt = authenticate_user(username, password)
        if login_attempt:
            # TODO: determine role
            clear()
            super_admin_menu()
            break
        else:
            clear()
            print("Wrong login credentials\n")
            continue
            
def signup_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        firstname = input("Enter your password\n")
        lastname = input("Enter your password\n")

welcome_screen()

# if check_password(entered_pw, user_hashed_pw):
#     print("Welcome, admin!")
#     role = get_user_role(username)
#     load_menu(role)
# else:
#     log_failed_login(username)
