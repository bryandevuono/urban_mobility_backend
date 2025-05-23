from service_engineer import menu as service_engineer_menu
def menu():
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