import os
import sys
from super_admin import menu as super_admin_menu
from getpass import getpass
sys.path.insert(0, '../auth')
from login import authenticate_user 
sys.path.insert(0, '../')
from logger import log_event
clear = print("------------------------------------------------------------------------------\n")

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
    while True:
        clear()
        print("Please enter your username and password to log in.\n")
        username = input("Enter your username\n")
        password = getpass("Enter your password (input is hidden)\n")
        authenticate_user(username, password)

welcome_screen()
