clear = lambda: os.system('clear')
def welcome_screen():
    print("Welcome to the urban mobility system\n"
           "Choose an option:\n"
           "\n Login (enter L)\n"
           "Register (enter R)")
    login_option = input()

    if (login_option.lower() == "l" and len(login_option) < 2):
        clear()
        login_screen()
    else:
        print("Wrong key, please try again")

def login_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        login = Auth.login.authenticate_user(username, password)

def signup_screen():
    while True:
        username = input("Enter your username\n")
        password = input("Enter your password\n")
        firstname = input("Enter your password\n")
        lastname = input("Enter your password\n")
