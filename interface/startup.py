import sys
from super_admin import menu as super_admin_menu
from getpass import getpass
sys.path.insert(0, '../auth')
from login import authenticate_user 
sys.path.insert(0, '../')
from logger import log_event
clear = lambda: print("------------------------------------------------------------------------------\n")

def welcome_screen():
    log_event("system", "User has entered the welcome screen", "0")
    while True:
        print("Welcome to the urban mobility system\n"
           "Choose an option:\n"
           "\nLogin (enter L)\n"
           "Exit (enter E)\n")
        login_option = input()
        if (login_option.lower() == "l" and len(login_option) < 2):
            clear()
            login_screen()
            break
        if (login_option.lower() == "e" and len(login_option) < 2):
            clear()
            print("Exiting the system. Goodbye!")
            sys.exit(0)
            break
        else:
            clear()
            print("Wrong key, please try again")
            continue

def login_screen():
    login_counter = 0
    log_event("system", "User has entered the login screen", "0")
    while True:
        print("Please enter your username and password to log in.\n")
        username = input("Enter your username\n")
        password = getpass("Enter your password (input is hidden)\n")
        authenticated = authenticate_user(username, password)

        if authenticated:
            clear()
            print("Login successful!")
            log_event("system", f"User {username} has logged in successfully", "0")

        else:
            login_counter += 1
            log_event("system", f"User {username} failed to log in", "1")
            if login_counter >= 3:
                clear()
                log_event("system", "User has failed to log in 3 times", "1")
                print("Too many failed attempts. Exiting the system.")
                sys.exit(0)
            else:
                print(f"Login failed. You have {3 - login_counter} attempts left.")

welcome_screen()
