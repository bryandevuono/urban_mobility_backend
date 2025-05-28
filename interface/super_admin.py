from service_engineer import menu as service_engineer_menu, search_scooter
from system_admin import menu as system_admin_menu
from system_admin import *
import os
sys.path.insert(0, '../')
from constants import *
import sys
sys.path.insert(0, '../crud')
from users import *

clear = lambda: os.system('cls')

def menu():
    print("Welcome to the Backend System, super admin!")
    # service_engineer
    service_engineer_menu()
    # system_admin
    system_admin_menu()
    #super_admin
    print("16: Add a new System Administrator to the backend system")
    print("17: Modify or update an existing System Administrator account and profile")
    print("18: Delete an existing System Administrator account")
    print("19: Reset an existing System Administrator password (temporary password)")
    print("20: Make a backup of the backend system")
    print("21: Restore a backup of the backend system")
    print("22: Generate a restore-code for a System Administrator and backup")
    print("23: Revoke a previously generated restore-code")
    print("0: Exit")
    print("Please select an option (0-23):")

    options = {
        "2": search_scooter,
        "3": display_users,
        "4": add_service_engineer,
        "6": delete_service_engineer,
        "12": add_scooter,
        "13": update_scooter,
        "14": delete_scooter,
        "16": add_system_admin,
        "18": delete_system_admin
    }

    while True:
        choice = input("Please enter your choice: ")
        if choice == "0":
            print("Exiting the backend system. Goodbye!")
            break
        elif choice in options:
            print(f"You selected option {choice}.")
            options[choice]()
        else:
            print("Invalid choice. Please try again.")

def add_system_admin():
    clear()
    print("Enter the info of the new system admin")
    username = input("username:")
    password = input("password:")
    firstname = input("firstname:")
    lastname = input("lastname:")
    role = SYSTEM_ADMIN
    create_user(username, password, firstname, lastname, role)

def delete_system_admin():
    clear()
    print("Give the username of the user you want to delete:")
    username = input("username:")
    delete_user(username, SYSTEM_ADMIN)