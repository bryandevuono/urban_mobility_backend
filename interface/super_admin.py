from service_engineer import menu as service_engineer_menu, search_scooter
from system_admin import menu as system_admin_menu
from system_admin import *
import os
sys.path.insert(0, '../')
from constants import *
import sys
sys.path.insert(0, '../crud')
from users import create_user, delete_user, update_profile, reset_password, read_users    

# clear = lambda: ('cls')
clear = lambda: print('------------------------------------------------------------------------------\n')

def menu():
    #service engineer
    clear()
    print("Welcome to the Backend System, super admin!")
    print("1: Update the attributes of scooters in the system")
    print("2: Search and retrieve the information of a scooter")
    print("3: Update your password")
    # system admin
    print("4: Check the list of users and their roles")
    print("5: Add a new Service Engineer to the backend system")
    print("6: Modify or update an existing Service Engineer account and profile")
    print("7: Delete an existing Service Engineer account")
    print("8: Reset an existing Service Engineer password (temporary password)")
    print("9: View backend system logs")
    print("10: Add a new Traveller to the backend system")
    print("11: Update the information of a Traveller")
    print("12: Delete a Traveller from the backend system")
    print("13: Add a new scooter to the backend system")
    print("14: Update the information of a scooter")
    print("15: Delete a scooter from the backend system")
    print("16: Search and retrieve the information of a Traveller")
    # super admin
    print("17: Add a new System Administrator to the backend system")
    print("18: Modify or update an existing System Administrator account and profile")
    print("19: Delete an existing System Administrator account")
    print("20: Reset an existing System Administrator password (temporary password)")
    print("21: Backup menu")
    print("E: Exit")
    print("Please select an option (0-20):")

    options = {
        "1": update_scooter_attr,
        "2": search_scooter,
        # "3": update_password, # This is not implemented in the super admin menu
        "4": display_users,
        "5": add_service_engineer,
        "6": change_profile_service_engineer,
        "7": delete_service_engineer,
        "8": reset_password_service_engineer,
        "9": system_admin_menu,  # Placeholder for backend system logs
        "10": add_traveller,
        "11": change_traveller,
        "12": delete_traveller,
        "13": add_scooter,
        "14": update_scooter,
        "15": delete_scooter,
        "16": search_traveller,
        "17": add_system_admin,
        "18": change_profile_system_admin,
        "19": delete_system_admin,
        "20": reset_password_system_admin,
        "21": backup_menu
    }

    while True:
        choice = input("Please enter your choice: ")
        if choice.lower() == "e":
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
    user_to_modify = input("user to modify:")
    username = input("username:")
    firstname = input("firstname:")
    lastname = input("lastname:")
    updated = update_profile(username, firstname, lastname, user_to_modify, role=SYSTEM_ADMIN)
    if updated:
        print("Profile updated successfully.")
    else:
        print("Failed to update profile. Please check the input data.")

def reset_password_system_admin():
    clear()
    print("Enter the username of the admin whose password you want to reset:")
    username = input()    
    new_password = reset_password(username, SYSTEM_ADMIN)
    print(new_password)