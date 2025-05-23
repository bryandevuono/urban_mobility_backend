from service_engineer import menu as service_engineer_menu
from system_admin import menu as system_admin_menu
def menu():
    print("Welcome to the Backend System, super admin!")
    # service_engineer
    service_engineer_menu()
    # system_admin
    system_admin_menu()
    #super_admin
    print("16: Add a new System Administrator to the backend system")
    print("17: Modify or update an existing System Administrator account and profile")
    print("18: Delete an existing System Administrator account")
    print("19: Reset an existing System Administrator password (temporary password)")
    print("20: Make a backup of the backend system")
    print("21: Restore a backup of the backend system")
    print("22: Generate a restore-code for a System Administrator and backup")
    print("23: Revoke a previously generated restore-code")
    print("0: Exit")