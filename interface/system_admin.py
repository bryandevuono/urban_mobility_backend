from service_engineer import menu as service_engineer_menu
import os
import sys
sys.path.insert(0, '../crud')

from scooters import add_scooter_info, update_scooter_info,delete_scooter_info, read_scooter_info
from users import create_user

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
    target_range_soc_min = int(input("Target Range SOC Min (%): "))
    target_range_soc_max = int(input("Target Range SOC Max (%): "))
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    out_of_service = int(input("Out of Service (0 for No, 1 for Yes): "))
    mileage = float(input("Mileage (km): "))
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD): ")

    add_scooter_info(brand, model, serial_number, top_speed, battery_capacity, soc, target_range_soc_min,
                    target_range_soc_max, latitude, longitude, out_of_service, mileage, last_maintenance_date)
    
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
    target_range_soc_min = input("Target Range SOC Min (%), leave blank to keep current: ")
    target_range_soc_max = input("Target Range SOC Max (%), leave blank to keep current: ")
    latitude = input("Latitude (leave blank to keep current): ")
    longitude = input("Longitude (leave blank to keep current): ")
    out_of_service = input("Out of Service (0 for No, 1 for Yes, leave blank to keep current): ")
    mileage = input("Mileage (km, leave blank to keep current): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD, leave blank to keep current): ")

    update_scooter_info(serial_number, brand, model, 
                   float(top_speed),
                   int(battery_capacity),
                   int(soc),
                   int(target_range_soc_min),
                   int(target_range_soc_max),
                   float(latitude),
                   float(longitude),
                   int(out_of_service),
                   float(mileage),
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