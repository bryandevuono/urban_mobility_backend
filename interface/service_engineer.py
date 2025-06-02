import os
import sys
sys.path.insert(0, '../crud')
from scooters import *
clear = lambda: os.system('cls')

def menu():
    # service_engineer
    print("Welcome, service engineer!")
    print("Please choose an option (number):")
    print("1: Update the attributes of scooters in the system")
    print("2: Search and retrieve the information of a scooter")

def update_scooter_attr():
    clear()
    print("Enter scooter information to update:")
    serial_number = input("Serial Number: ")
    brand = input("Brand: ")
    model = input("Model: ")
    top_speed = input("Top Speed (km/h): ")
    battery_capacity = input("Battery Capacity (Wh): ")
    state_of_charge = input("State of Charge (%): ")
    target_range_soc = input("Target Range at SOC (%): ")
    location = input("Location: ")
    out_of_service = input("Out of Service (yes/no): ").lower() == 'yes'
    mileage = input("Mileage (km): ")
    last_maintenance_date = input("Last Maintenance Date (YYYY-MM-DD): ")

    updated = update_scooter_info(serial_number, brand, model, top_speed,battery_capacity,state_of_charge,target_range_soc,
                                location,out_of_service,mileage,last_maintenance_date)
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
    print("Search completed. Check the logs for details.")