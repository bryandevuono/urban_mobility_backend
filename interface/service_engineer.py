import os
import sys
from getpass import getpass
sys.path.insert(0, '../crud')
from scooters import update_scooter_info, read_scooter_info
from users import modify_password

# clear = lambda: ('cls')
clear = lambda: print('------------------------------------------------------------------------------\n')

def menu(username):
    while True:
        # service_engineer
        clear()
        print("Welcome, service engineer!\n")
        print("Please choose an option (number):")
        print("1: Update the attributes of scooters in the system")
        print("2: Search and retrieve the information of a scooter")
        print("3: Update your password")
        print("E: Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            update_scooter_attr()
            break
        elif choice == '2':
            search_scooter()
            break
        elif choice == '3':
            update_password(username)
        elif choice.lower() == 'e':
            sys.exit(0)
            break
        else:
            print("Invalid choice. Please try again.")

def update_scooter_attr():
    # the data to update a scooter is limited for a service engineer
    clear()
    print("Enter scooter information to update:")
    state_of_charge = input("State of Charge (%): ")
    target_range_soc = input("Target Range at SOC (%): ")
    location = input("Location: ")
    out_of_service = input("Out of Service (0/1): ")
    mileage = input("Mileage (km): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD): ")

    updated = update_scooter_info(serial_number=None, brand=None, model=None, top_speed=None,battery_capacity=None,state_of_charge=state_of_charge,target_range_soc=target_range_soc,
                                location=location,out_of_service=out_of_service,mileage=mileage,last_maintenance_date=last_maintenance_date)
    if updated:
        print("Scooter info updated!")
    else:
        print("Something went wrong while trying to update...")
        
def search_scooter():
    clear()
    print("Enter scooter information to search:")
    input_param = input("Search Parameter (Brand, Model, Serial Number, etc.): ")
    scooter_result = read_scooter_info(input_param)
    print(scooter_result)
    print("Search completed.")

def update_password(username):
    clear()
    print("Enter your old password:")
    old_password = getpass("Enter you old password:")
    print("Enter your new password:")
    new_password = getpass("New Password: ")
    modified = modify_password(old_password, new_password, username)
    if modified:
        print("Password updated successfully!")
    else:
        print("Something went wrong while trying to update the password.")