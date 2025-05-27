import os
import sys
sys.path.insert(0, '../crud')
from scooters import read_scooter_info
clear = lambda: os.system('cls')

def menu():
    # service_engineer
    print("Welcome, service engineer!")
    print("Please choose an option (number):")
    print("1: Update the attributes of scooters in the system")
    print("2: Search and retrieve the information of a scooter")

def search_scooter():
    clear()
    print("Enter scooter information to search:")
    input_param = input("Search Parameter (Brand, Model, Serial Number, etc.): ")
    scooter_result = read_scooter_info(input_param)
    print(scooter_result)
    print("Search completed. Check the logs for details.")