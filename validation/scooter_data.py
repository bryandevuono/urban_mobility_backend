import re
max_input_length = 50 # to prevent buffer overflow

def validate_brand(brand) -> bool:
    if len(brand) < max_input_length and len(brand) > 0 and brand.isalpha():
        return True
    else:
        return False
    
def validate_model(model) -> bool:
    if len(model) < max_input_length and len(model) > 0 and model.isalnum():
        return True
    else:
        return False
    
def validate_serial_number(serial_number) -> bool:
    if len(serial_number) < 18 and len(serial_number) > 9 and serial_number.isalnum():
        return True
    else:
        return False
    
def validate_top_speed(speed):
    if len(speed) > 0 and len(speed) < 4 and speed.isdigit():
        return True
    else:
        return False

def validate_battery_capacity(capacity):    
    if len(capacity) > 0 and len(capacity) < 6 and capacity.isdigit():
        return True
    else:
        return False

def validate_state_of_charge(soc):
    if len(soc) > 0 and len(soc) < 4 and soc.isdigit() and 0 <= int(soc) <= 100:
        return True
    else:
        return False
    
def validate_location(location):
    regex_location = "^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$"
    if len(location) < max_input_length and len(location) > 0 and location.isalnum() and re.match(regex_location, location):
        return True
    else: 
        return False
    
def validate_out_of_service(out_of_service):
    if out_of_service in ['0', '1']:
        return True
    else:
        return False
    
def validate_mileage(mileage):
    if len(mileage) > 0 and len(mileage) < 7 and mileage.isdigit():
        return True
    else:
        return False
    
def validate_last_maintenance_date(date):
    regex_date = r"^\d{4}-\d{2}-\d{2}$"
    if len(date) == 10 and re.match(regex_date, date):
        return True
    else:
        return False