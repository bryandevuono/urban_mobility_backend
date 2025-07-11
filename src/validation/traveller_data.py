import re
def validate_name(name):
    if len(name) > 0 and len(name) < 36 and name.isalpha():
        return True
    else:
        print("\nName must be between 1 and 35 characters long. Use only alphabetic characters.")
        return False
    
def validate_gender(gender):
    if gender.upper() in ['M', 'F', 'O']:
        return True
    else:
        print("\nPlease enter a valid gender option ('M', 'F', or 'O').")
        return False

def validate_birthday(birthday):
    regex_date = r"^\d{4}-\d{2}-\d{2}$"
    if len(birthday) == 10 and re.match(regex_date, birthday):
        return True
    else:
        print("\nInvalid date format. It should be in the format 'YYYY-MM-DD'.")
        return False
    
def validate_house_number(house_number):
    if len(house_number) > 0 and len(house_number) < 4 and house_number.isalnum():
        return True
    else:
        print("\nHouse number must be between 1 and 3 characters long and can only contain alphanumeric characters.")
        return False
    
def validate_zip_code(zip_code):
    #zip code is DDDDXX
    zipcode_re = r'\d{4}[ ]?[A-Z]{2}'
    if len(zip_code) == 6 and re.match(zipcode_re, zip_code.upper()):
        return True
    else:
        print("\nZip code must be exactly 5 digits long and follow the format XXXXDD.")
        return False
    
def validate_city(city):
    cities = ['amsterdam', 'rotterdam', 'the hague', 'utrecht', 'eindhoven', 'tilburg', 'groningen', 'almere', 'breda', 'nijmegen']
    if city.lower() in cities:
        return True
    else:
        print("\nPlease enter a valid city from the list: " + ", ".join(cities))
        return False
    
def validate_email(email):
    email_re = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if len(email) > 0 and re.match(email_re, email):
        return True
    else:
        print("\nPlease enter a valid email address.")
        return False
    
def validate_phone_number_nl(phone_number):
    phone_number_re = r'^(?:\+31|0)[1-9]\d{8}$'
    if re.match(phone_number_re, phone_number):
        return True
    else:
        print("\nPlease enter a valid Dutch phone number starting with +31 or 0, followed by 9 digits.")
        return False
    
def validate_driver_license_number(license_number):
    license_number_re = r'^([A-Z]{2}\d{6,7}|[A-Z]{1}\d{7,8})$'
    if re.match(license_number_re, license_number):
        return True
    else:
        print("\nDriver's license number must be in the format 'XX123456', where 'XX' are uppercase letters and '123456' are digits.")
        return False