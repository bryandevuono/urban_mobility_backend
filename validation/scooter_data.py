import re
max_input_length = 50 # to prevent buffer overflow

def validate_brand(brand) -> bool:
    if len(brand) < max_input_length and len(brand) > 0 and brand.isalpha():
        return True
    else:
        print("Invalid brand name. It should be alphabetic and less than 50 characters.")
        return False
    
def validate_model(model) -> bool:
    if len(model) < max_input_length and len(model) > 0 and model.isalnum():
        return True
    else:
        print("Invalid model name. It should be alphanumeric and less than 50 characters.")
        return False
    
def validate_serial_number(serial_number) -> bool:
    if len(serial_number) < 18 and len(serial_number) > 9 and serial_number.isalnum():
        return True
    else:
        print("Invalid serial number. It should be alphanumeric and between 10 to 17 characters.")
        return False
    
def validate_top_speed(speed):
    if len(speed) > 0 and len(speed) < 4 and speed.isdigit():
        return True
    else:
        print("Invalid top speed. It should be a number between 1 and 999.")
        return False

def validate_battery_capacity(capacity):    
    if len(capacity) > 0 and len(capacity) < 6 and capacity.isdigit():
        return True
    else:
        print("Invalid battery capacity. It should be a number between 1 and 99999.")
        return False

def validate_state_of_charge(soc):
    if len(soc) > 0 and len(soc) < 4 and soc.isdigit() and 0 <= int(soc) <= 100:
        return True
    else:
        print("Invalid state of charge. It should be a number between 0 and 100.")
        return False
    
def validate_location(location):
    location_pattern = r'^[-+]?[0-9]*\.?[0-9]+$'
    if len(location) < max_input_length and len(location) > 0 and re.match(location_pattern, location):
        return True
    else: 
        print("Invalid location format. It should be in the format 'latitude, longitude' (e.g., '37.7749, -122.4194').")
        return False
    
def validate_out_of_service(out_of_service):
    if out_of_service in ['0', '1']:
        return True
    else:
        print("Invalid out of service value. It should be '0' (not out of service) or '1' (out of service).")
        return False
    
def validate_mileage(mileage):
    if len(mileage) > 0 and len(mileage) < 7 and mileage.isdigit():
        return True
    else:
        print("Invalid mileage. It should be a number between 1 and 999999.")
        return False
    
def validate_last_maintenance_date(date):
    regex_date = r"^\d{4}-\d{2}-\d{2}$"
    if len(date) == 10 and re.match(regex_date, date):
        return True
    else:
        print("Invalid date format. It should be in the format 'YYYY-MM-DD'.")
        return False
    
def validate_search_parameter(input_param):
    if len(input_param) < max_input_length and len(input_param) > 0:
        return True
    else:
        print("Invalid search parameter. It should be less than 50 characters.")
        return False