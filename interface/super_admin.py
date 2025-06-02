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
    # service_engineer 'inheritance'
    service_engineer_menu()
    # system_admin 'inheritance'
    system_admin_menu()
    #super_admin
    print("16: Add a new System Administrator to the backend system")
    print("17: Modify or update an existing System Administrator account and profile")
    print("18: Delete an existing System Administrator account")
    print("19: Reset an existing System Administrator password (temporary password)")
    print("20: Backup menu")
    print("0: Exit")
    print("Please select an option (0-20):")

    options = {
        "2": search_scooter,
        "3": display_users,
        "4": add_service_engineer,
        "5": change_profile_service_engineer,
        "6": delete_service_engineer,
        "9": add_traveller,
        "10": change_traveller,
        "11": delete_traveller,
        "12": add_scooter,
        "13": update_scooter,
        "14": delete_scooter,
        "15": search_traveller,
        "16": add_system_admin,
        "17": change_profile_system_admin,
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

def backup_menu():
    clear()
    print("------------ Backup Menu ------------")
    print("1: Create a backup of the database")
    print("2: Restore the database from a backup")
    print("3: Allow a specific System Administrator to restore a specific backup.")
    print("4: To revoke a previously generated restore-code for a System Administrator.")

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

def change_profile_system_admin():
    clear()
    print("Enter the info of the system admin you want to change:")
    username = input("username:")
    firstname = input("firstname:")
    lastname = input("lastname:")
    user_to_modify = input("user to modify:")
    update_profile_admin(username, firstname, lastname, user_to_modify)