from service_engineer import menu as service_engineer_menu
from service_engineer import *
import os
import sys
sys.path.insert(0, '../')
from constants import *
sys.path.insert(0, '../crud')

from scooters import add_scooter_info, update_scooter_info,delete_scooter_info, read_scooter_info
from users import create_user, delete_user, update_profile, reset_password, read_users
from travellers import create_traveller, update_traveller, read_traveller, remove_traveller

# TODO: add validation for inputs
clear = lambda: os.system('cls')

def menu(username):
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

    options = {
        '1': update_scooter_attr,
        '2': search_scooter,
        '3': update_password,
        '4': display_users,
        '5': add_service_engineer,
        '6': change_profile_service_engineer,
        '7': delete_service_engineer,
        '8': reset_password_service_engineer(username),
        '9': "",  # TODO: Implement view backend system logs
        '10': add_traveller,
        '11': change_traveller,
        '12': delete_traveller,
        '13': add_scooter,
        '14': update_scooter,
        '15': delete_scooter,
        '16': search_traveller,
        'e': lambda: sys.exit(0)  # Exit option
    }
    while True:
        choice = input("Enter your choice (3-15): ")
        if choice in options:
            clear()
            options[choice]()
        elif choice.lower() == 'e':
            print("Exiting the system. Goodbye!")
            sys.exit(0)
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
    
def update_scooter():
    clear()
    print("Enter the scooter serial number to update:")
    serial_number = input("Serial Number: ")
    
    brand = input("Brand (leave blank to keep current): ")
    model = input("Model (leave blank to keep current): ")
    top_speed = input("Top Speed (km/h, leave blank to keep current): ")
    battery_capacity = input("Battery Capacity (mAh, leave blank to keep current): ")
    soc = input("State of Charge (%), leave blank to keep current: ")
    target_range_soc = input("Target Range SOC (%), leave blank to keep current: ")
    location = input("Location, leave blank to keep current:")
    out_of_service = input("Out of Service (0 for No, 1 for Yes, leave blank to keep current): ")
    mileage = input("Mileage (km, leave blank to keep current): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD, leave blank to keep current): ")

    updated = update_scooter_info(serial_number, 
                                brand, 
                                model, 
                                top_speed,
                                battery_capacity,
                                soc,
                                target_range_soc,
                                location,
                                out_of_service,
                                mileage,
                                last_maintenance_date)
    if updated:
        print("Scooter updated successfully!")
    else:
        print("Scooter not found or update failed. Please check the serial number and input values.")
        return
    
    print("Scooter updated successfully!")

def delete_scooter():
    clear()
    print("Enter the scooter serial number to delete:")
    serial_number = input("Serial Number: ")

    confirmation = input(f"Are you sure you want to delete the scooter with Serial Number {serial_number}? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        delete_scooter_info(serial_number)
        print("Scooter deleted successfully!")
    else:
        print("Operation cancelled.")

def add_service_engineer():
    clear()
    print("Enter the info of the new service engineer:")
    username = input("Username:")
    password = input("password:")
    role = "service_engineer" # make const
    first_name = input("first_name:")
    last_name = input("last_name:")
    create_user(username, password, first_name, last_name, role)

def display_users():
    clear()
    print("Users:")
    users = read_users()
    print("id", "username", "firstname", "role", "lastname", "created_date")
    for user in users:
        print(user)

def delete_service_engineer():
    clear()
    print("Enter the username of the service engineer you want to delete:")
    username = input()
    deleted = delete_user(username, "service_engineer")
    if deleted:
        print(f"Service Engineer {username} deleted successfully.")
    else:
        print(f"Service Engineer {username} not found or deletion failed.")

def add_traveller():
    clear()
    print("Enter the info of the new traveller:")
    first_name = input("firstname:")
    last_name = input("lastname:")
    birth_date = input("birth_date (YYYY-MM-DD):")
    email = input("email:")
    phone_number = input("phone_number:")
    gender = input("Gender (M/F):")
    streetname = input("Street Name:")
    house_number = input("Street Number:")
    zip_code = input("Zip Code:")
    city = input("City ('Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven', 'Tilburg', 'Groningen', 'Almere', 'Breda', 'Nijmegen'):")
    driving_license_number = input("Driving License Number:")
    create_traveller(first_name, last_name, birth_date, email, phone_number, gender, streetname, 
                house_number, zip_code, city, driving_license_number)

def delete_traveller():
    clear()
    print("Enter the email of the traveller you want to delete:")
    email = input()
    removed = remove_traveller(email)
    if removed:
        print(f"Traveller with email {email} deleted successfully.")
    else:
        print(f"Traveller with email {email} not found or deletion failed.\n Check if the email is valid and exists in the system.")

def search_traveller():
    clear()
    print("Enter the info of the traveller you want to search:")
    search_param = input()
    traveller = read_traveller(search_param)
    if traveller:
        print("Result", traveller)
    else:
        print("Traveller not found.")

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
    print("Traveller updated successfully!")
    
def change_profile_service_engineer():
    clear()
    user_to_modify = input("Enter the username of the service engineer you want to modify:")
    firstname = input("New First Name (leave blank to keep current): ")
    lastname = input("New Last Name (leave blank to keep current): ")
    username = input("New username of the service engineer to modify: ")
    update_profile(username, firstname, lastname, user_to_modify, SERVICE_ENGINEER)

def reset_password_service_engineer():
    clear()
    print("Enter the username of the service engineer whose password you want to reset:")
    username = input()    
    new_password = reset_password(username, SERVICE_ENGINEER)
    print(new_password)