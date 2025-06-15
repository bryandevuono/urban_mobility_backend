import os
import sys
from getpass import getpass
sys.path.insert(0, './crud')
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
        elif choice == '2':
            search_scooter()
        elif choice == '3':
            update_password(username)
        elif choice.lower() == 'e':
            break
        else:
            print("Invalid choice. Please try again.")

def update_scooter_attr():
    # the data to update a scooter is limited for a service engineer
    clear()
    print("Enter scooter information to update:")
    serial_no = input("Serial Number for the scooter to update: ")
    state_of_charge = input("State of Charge (%) (Leave empty to keep it unchanged): ")
    target_range_soc = input("Target Range at SOC (%) (Leave empty to keep it unchanged): ")
    location = input("Location (Leave empty to keep it unchanged): ")
    out_of_service = input("Out of Service (0/1) (Leave empty to keep it unchanged): ")
    mileage = input("Mileage (km) (Leave empty to keep it unchanged): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD) (Leave empty to keep it unchanged): ")

    updated = update_scooter_info(serial_number=serial_no, brand="", model="", top_speed="",battery_capacity="",soc=state_of_charge,target_range_soc=target_range_soc,
                                location=location,out_of_service=out_of_service,mileage=mileage,last_maintenance_date=last_maintenance_date, new_serial_no="")
    if updated:
        print("\nScooter info updated!")
    else:
        print("Something went wrong while trying to update...")
        
def search_scooter():
    clear()
    print("Enter scooter information to search:")
    input_param = input("Search Parameter (Brand, Model, Serial Number, etc.): ")
    scooter_result = read_scooter_info(input_param)
    print("\n(id, brand, model, serial_no, top_speed, battery_capacity, state_of_charge, target_range, location, out of service (0/1), mileage):")
    if scooter_result:
        print(scooter_result)
    else:
        print("\nNo scooters found matching the search criteria.")
    print("Search completed.")

def update_password(username):
    clear()
    print("To update your password, please enter your old password and the new password you want to set:")
    old_password = getpass("Enter you old password:")
    print("Enter your new password:")
    new_password = getpass("New Password: ")
    modified = modify_password(old_password, new_password, username)
    if modified:
        print("Password updated successfully!")
    else:
        print("Something went wrong while trying to update the password.")