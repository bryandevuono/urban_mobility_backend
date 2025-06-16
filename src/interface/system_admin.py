from service_engineer import menu as service_engineer_menu
from service_engineer import *
import os
import sys
sys.path.insert(0, './')
from logger import read_logs
from constants import *
from getpass import getpass
sys.path.insert(0, './crud')
from logger import log_event, set_username
from scooters import add_scooter_info, update_scooter_info,delete_scooter_info, read_scooter_info
from users import create_user, delete_user, update_profile, reset_password, read_users
from travellers import create_traveller, update_traveller, read_traveller, remove_traveller
sys.path.insert(0, './database')

from backup import backup_database, restore_database, create_restore_code, revoke_restore_code
import os

clear = lambda: print('------------------------------------------------------------------------------\n')

def menu(username):
    while True:
        set_username(username)
        clear()
        print("Welcome to the Backend System, System Admin!")
        print("1: Update the attributes of scooters in the system")
        print("2: Search and retrieve the information of a scooter")
        print("3: Update your password")
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
        print("17: Backup and restore the database")
        print("E: Exit the system")
        print("------------------------------------------------------------------------------")

        options = {
            '1': update_scooter_attr,
            '2': search_scooter,
            '3': lambda: update_password(username),
            '4': lambda: display_users(role=SYSTEM_ADMIN),
            '5': add_service_engineer,
            '6': change_profile_service_engineer,
            '7': delete_service_engineer,
            '8': reset_password_service_engineer,
            '9': see_logs,
            '10': add_traveller,
            '11': change_traveller,
            '12': delete_traveller,
            '13': add_scooter,
            '14': update_scooter_attr_admin,
            '15': delete_scooter,
            '16': search_traveller,
        }
        choice = input("Enter your choice (1-17): ")
        if choice in options:
            clear()
            options[choice]()
        elif choice.lower() == '17':    
            backup_menu(SYSTEM_ADMIN, username)
        elif choice.lower() == 'e':
            break
        else:
            print("Invalid choice. Please try again.")

def add_scooter():
    clear()
    print("Enter the scooter info:")
    brand = input("Brand: ")
    model = input("Model: ")
    serial_number = input("Serial Number: ")
    top_speed = (input("Top Speed (km/h): "))
    battery_capacity = (input("Battery Capacity (mAh): "))
    soc = (input("State of Charge (%): "))
    target_range_soc = (input("Target Range SOC Min (%): "))
    location = (input("location: "))
    out_of_service = (input("Out of Service (0 for No, 1 for Yes): "))
    mileage = (input("Mileage (km): "))
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD): ")

    added = add_scooter_info(brand, model, serial_number, top_speed, battery_capacity, soc, target_range_soc,
                    location, out_of_service, mileage, last_maintenance_date)
    if added:
        print("\nScooter added successfully!")
    else: 
        print("\nSomething went wrong while trying to add the scooter. Please check the input values.")
    

def delete_scooter():
    clear()
    print("Enter the scooter serial number to delete:")
    serial_number = input("Serial Number: ")

    confirmation = input(f"Are you sure you want to delete the scooter with Serial Number {serial_number}? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        deleted = delete_scooter_info(serial_number)
        if deleted:
            print("Scooter deleted successfully!")
        else: 
            print("Failed to delete the scooter. Please check if the Serial Number is correct and exists in the system.")
    else:
        print("Operation cancelled.")

def add_service_engineer():
    clear()
    print("Enter the info of the new service engineer:")
    username = input("Username (8-10 characters):")
    password = getpass("password (Password must be between 12 and 30 characters long, contain at least one digit, one lowercase letter, one uppercase letter, and one special character.):")
    role = SERVICE_ENGINEER
    first_name = input("first_name:")
    last_name = input("last_name:")
    created = create_user(username, password, first_name, last_name, role)
    if created:
        print("Service Engineer created successfully.")
    else:
        print("\nFailed to create Service Engineer. Please check the input data.")

def display_users(role):
    clear()
    print("Users:")
    users = read_users(role)
    print("id", "username", "firstname", "role", "lastname", "created_date")
    for user in users:
        print(user)

def delete_service_engineer():
    clear()
    display_users(SYSTEM_ADMIN)
    print("Enter the user_id of the service engineer you want to delete (see overview):")
    id = input()
    deleted = delete_user(id, "service_engineer")
    if deleted:
        print(f"\nService Engineer deleted successfully.")
    else:
        print(f"\nService Engineer not found or deletion failed. Make sure the ID is valid and exists in the system.")

def add_traveller():
    clear()
    print("Enter the info of the new traveller:")
    firstname = input("firstname:")
    lastname = input("lastname:")
    birthday = input("birth_date (YYYY-MM-DD):")
    email_address = input("email:")
    mobile_phone = input("phone_number:")
    gender = input("Gender (M/F):")
    streetname = input("Street Name:")
    house_number = input("Street Number:")
    zip_code = input("Zip Code (XXXXDD):")
    city = input("City ('Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven', 'Tilburg', 'Groningen', 'Almere', 'Breda', 'Nijmegen'):")
    driving_license_number = input("Driving License Number:")
    created = create_traveller(firstname, lastname, birthday, gender, streetname, house_number, 
                            zip_code, city, email_address, mobile_phone, driving_license_number)
    if created:
        print("Traveller created successfully.")
    else:
        print("\nFailed to create Traveller. Please check the input data and ensure all fields are valid.")

def delete_traveller():
    clear()
    print("Enter the email of the traveller you want to delete:")
    email = input()
    removed = remove_traveller(email)
    if removed:
        print(f"Traveller with email {email} deleted successfully.")
    else:
        print(f"Traveller with email {email} not found or deletion failed.\nCheck if the email is valid and exists in the system.")

def search_traveller():
    clear()
    print("Enter the info of the traveller you want to search:")
    search_param = input()
    read_traveller(search_param)

def change_traveller():
    clear()
    print("Enter the email of the traveller you want to update:")
    email_to_search = input()
    first_name = input("First Name (leave blank to keep current): ")
    last_name = input("Last Name (leave blank to keep current): ")
    birth_date = input("Birth Date (YYYY-MM-DD, leave blank to keep current): ")
    phone_number = input("Phone Number (leave blank to keep current): ")
    gender = input("Gender (M/F, leave blank to keep current): ")
    streetname = input("Street Name (leave blank to keep current): ")
    house_number = input("House Number (leave blank to keep current): ")
    zip_code = input("Zip Code (leave blank to keep current): ")
    city = input("City (leave blank to keep current): ")
    driving_license_number = input("Driving License Number (leave blank to keep current): ")
    email_address = input("Email Address (leave blank to keep current): ")

    updated = update_traveller(
        email_to_search,
        email_address,
        first_name,
        last_name,
        birth_date,
        phone_number,
        gender,
        streetname,
        house_number,
        zip_code,
        city,
        driving_license_number
    )
    if not updated:
        print("Traveller not found or update failed.")
        return
    print("\nTraveller updated successfully!")
    
def change_profile_service_engineer():
    clear()
    display_users(SYSTEM_ADMIN)
    print("Enter the user_id of the service engineer you want to modify (see overview):")
    id = input("Enter the ID:")
    firstname = input("\nNew First Name (leave blank to keep current): ")
    lastname = input("New Last Name (leave blank to keep current): ")
    username = input("New username of the service engineer to modify (Leave blank to keep current): ")
    updated = update_profile(username, firstname, lastname, id, SERVICE_ENGINEER)
    if updated:
        print(f"\nService Engineer updated successfully!")
    else:
        print(f"\nFailed to update Service Engineer. Please check the input data and ensure the username is valid.")

def reset_password_service_engineer():
    clear()
    display_users(SYSTEM_ADMIN)
    print("Enter the user_id of the service engineer you want to reset (see overview):")
    id = input()    
    new_password = reset_password(id, SERVICE_ENGINEER)
    print(new_password)

def update_scooter_attr_admin():
    # the data to update a scooter is limited for a service engineer
    clear()
    print("Enter scooter information to update:")
    serial_number = input("Serial Number of the scooter to update: ")
    brand = input("Brand (Leave blank to keep current): ")
    model = input("Model (Leave blank to keep current): ")
    top_speed = input("Top Speed (km/h) (Leave blank to keep current): ")
    battery_capacity = input("Battery Capacity (Wh) (Leave blank to keep current): ")
    state_of_charge = input("State of Charge (%) (Leave blank to keep current): ")
    target_range_soc = input("Target Range at SOC (%) (Leave blank to keep current): ")
    location = input("Location: (Leave blank to keep current)")
    out_of_service = input("Out of Service (0/1) (Leave blank to keep current): ")
    mileage = input("Mileage (km) (Leave blank to keep current): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD) (Leave blank to keep current): ")
    new_serial_no = input("New Serial Number (Leave blank to keep current): ")
    updated = update_scooter_info(serial_number, brand, model, top_speed,battery_capacity,state_of_charge,target_range_soc,
                                location,out_of_service,mileage,last_maintenance_date, new_serial_no)
    if updated:
        print("\nScooter info updated!")
    else:
        print("Something went wrong while trying to update...")

def backup_menu(role, username):
    clear()
    while True:
        print("\n------------ Backup Menu ------------")
        print("1: Create a backup of the database")
        print("2: Restore the database from a backup")
        if role == SUPER_ADMIN:
            print("3: Allow a specific System Administrator to restore a specific backup.")
            print("4: To revoke a previously generated restore-code for a System Administrator.")
        print("E: Exit the backup menu")
        option = input("Please select an option: ")
        if option == "1":
            backup_database()
        elif option == "2":
            if role == 'system_admin':
                print("Enter the restore code:")
                restore_code = input("Restore Code: ")
            else:
                restore_code = None
            print("\nEnter the path to the backup file:")
            print("----------------------------------")
            print("Available backups:")
            backups = os.listdir('./database/backups')
            for backup in backups:
                print(backup)
            backup_filename = input("Backup name: ") + ".zip"
            restored = restore_database(backup_filename, restore_code, username, role)
            if restored:
                print("Database restored successfully!")
            else:
                print("Failed to restore the database. Please check the restore code and backup file.")
        elif option == "3" and role == SUPER_ADMIN:
            print("Enter the username of the admin who will be allowed to restore:")
            admin_username = input("Username: ")
            restore_code = create_restore_code(admin_username)
            print(f"restore_code: {restore_code}")
        elif option == "4" and  role == SUPER_ADMIN:
            print("Enter the username of the admin whose restore code you want to revoke:")
            admin_username = input("Username: ")
            revoked = revoke_restore_code(admin_username)
            if revoked:
                print(f"Restore code for {admin_username} has been revoked successfully.")
            else:
                print(f"Failed to revoke restore code for {admin_username}.")
        elif option.lower() == "e":
            print("Exiting the backup menu.")
            break
        else:
            print("Invalid option. Please try again.")

def see_logs():
    clear()
    read_logs()