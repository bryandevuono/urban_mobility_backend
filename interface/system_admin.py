from service_engineer import menu as service_engineer_menu
import os
import sys
sys.path.insert(0, '../crud')

from scooters import add_scooter_info, update_scooter_info,delete_scooter_info, read_scooter_info
from users import create_user, read_users, delete_user
from travellers import *

# TODO: add validation for inputs
clear = lambda: os.system('cls')

def menu():
    clear()
    print("Welcome to the Backend System, System Admin!")
    #service_engineer_menu
    service_engineer_menu()
    #system_admin
    print("3: Check the list of users and their roles")
    print("4: Add a new Service Engineer to the backend system")
    print("5: Modify or update an existing Service Engineer account and profile")
    print("6: Delete an existing Service Engineer account")
    print("7: Reset an existing Service Engineer password (temporary password)")
    print("8: View backend system logs")
    print("9: Add a new Traveller to the backend system")
    print("10: Update the information of a Traveller")
    print("11: Delete a Traveller from the backend system")
    print("12: Add a new scooter to the backend system")
    print("13: Update the information of a scooter")
    print("14: Delete a scooter from the backend system")
    print("15: Search and retrieve the information of a Traveller")

def add_scooter():
    clear()
    print("Enter the scooter info:")
    brand = input("Brand: ")
    model = input("Model: ")
    serial_number = input("Serial Number: ")
    top_speed = float(input("Top Speed (km/h): "))
    battery_capacity = int(input("Battery Capacity (mAh): "))
    soc = int(input("State of Charge (%): "))
    target_range_soc = int(input("Target Range SOC Min (%): "))
    location = float(input("location: "))
    out_of_service = int(input("Out of Service (0 for No, 1 for Yes): "))
    mileage = float(input("Mileage (km): "))
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD): ")

    add_scooter_info(brand, model, serial_number, top_speed, battery_capacity, soc, target_range_soc,
                    location, out_of_service, mileage, last_maintenance_date)
    
    print("Scooter added successfully!")
    
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

    update_scooter_info(serial_number, 
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
    create_user(username, password, role, first_name, last_name)

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
    delete_user(username, "service_engineer")

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
    city = input("City:")
    driving_license_number = input("Driving License Number:")
    create_traveller(first_name, last_name, birth_date, email, phone_number, gender, streetname, 
                house_number, zip_code, city, driving_license_number)

def delete_traveller():
    clear()
    print("Enter the email of the traveller you want to delete:")
    email = input()
    remove_traveller(email)

def search_traveller():
    clear()
    print("Enter the info of the traveller you want to search:")
    search_param = input()
    traveller = read_traveller(search_param)
    if traveller:
        print("Traveller found:", traveller)
    else:
        print("Traveller not found.")