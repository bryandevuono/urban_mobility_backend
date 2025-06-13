import sqlite3
import sys
sys.path.insert(0, '../validation')
from scooter_data import validate_brand, validate_model, validate_serial_number, \
    validate_top_speed, validate_battery_capacity, validate_state_of_charge, \
    validate_location, validate_out_of_service, validate_mileage, validate_last_maintenance_date

def add_scooter_info(brand, model, serial_number, top_speed, battery_capacity, soc, target_range_soc,
                    location, out_of_service, mileage, last_maintenance_date) -> bool:
    
    #validate inputs
    validators = [
        validate_brand(brand),
        validate_model(model),
        validate_serial_number(serial_number),
        validate_top_speed(top_speed), 
        validate_battery_capacity(battery_capacity),
        validate_state_of_charge(soc),
        validate_state_of_charge(target_range_soc),
        validate_location(location), 
        validate_out_of_service(out_of_service),
        validate_mileage(mileage),
        validate_last_maintenance_date(last_maintenance_date)
    ]
    
    for validator in validators:
        if validator:
            pass
        else:
            return False
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO scooter_data (
            brand, model, serial_number, top_speed, battery_capacity, state_of_charge,
            target_range_soc, location,
            out_of_service, mileage, last_maintenance_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (brand,model,serial_number,float(top_speed),float(battery_capacity),int(soc),int(target_range_soc),float(location),
              int(out_of_service),float(mileage),last_maintenance_date)
        )

    conn.commit()
    conn.close()

    return True


def update_scooter_info(serial_number, brand, model, top_speed,battery_capacity,soc,target_range_soc,
                        location,out_of_service,mileage,last_maintenance_date, new_serial_no) -> bool:
    # check if serial number exists
    if validate_serial_number(serial_number):
        pass
    else:
        print("\nInvalid serial number format. Please try again.")
        return False
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM scooter_data
        WHERE serial_number = ?
    ''', (serial_number,))
    scooter = cursor.fetchone()
    if scooter:
        pass
    else:
        conn.close()
        print("\nScooter with this serial number does not exist.")
        return False
    
    query = "UPDATE scooter_data SET "

    params = []
    if len(brand) > 0 and validate_brand(brand):
        query += ', brand = ? '
        params.append(brand)
    if len(model) > 0 and validate_model(model):
        query += ', model = ? '
        params.append(model)
    if len(top_speed) > 0 and validate_top_speed(top_speed):
        query += ', top_speed = ? '
        params.append(float(top_speed))
    if len(battery_capacity) > 0 and validate_battery_capacity(battery_capacity):
        query += ', battery_capacity = ? '
        params.append(float(battery_capacity))
    if len(soc) > 0 and validate_state_of_charge(soc):
        query += ', state_of_charge = ? '
        params.append(int(soc))
    if len(target_range_soc) > 0 and validate_state_of_charge(target_range_soc):
        query += ', target_range_soc = ? '
        params.append(int(target_range_soc))
    if len(location) > 0 and validate_location(location):
        query += ', location = ?, '
        params.append(float(location))
    if len(out_of_service) > 0 and validate_out_of_service(out_of_service):
        query += ', out_of_service = ? '
        params.append(int(out_of_service))
    if len(mileage) > 0 and validate_mileage(mileage):
        query += ', mileage = ?'
        params.append(float(mileage))
    if len(last_maintenance_date) > 0 and validate_last_maintenance_date(last_maintenance_date):
        query += ', last_maintenance_date = ? '
        params.append(last_maintenance_date)
    if new_serial_no and validate_serial_number(new_serial_no):
        query += ', serial_number = ? '
        params.append(new_serial_no)
    #check if any fields were given to update
    if len(params) == 0:
        print("\nNo fields were provided to update. Please provide at least one field to update.")
        conn.close()
        return False
    #remove first comma of query
    query = query.replace(", ", " ", 1)
    # add serial number to search the scooter
    params.append(serial_number)
    query += 'WHERE serial_number = ? '
    cursor.execute(query, params)
    conn.commit()
    
    if cursor.rowcount > 0:
        conn.close()
        return True
    else:
        print("\nNo changes were made to the scooter information. Some fields may not have been updated due to validation errors.")
        conn.close()
        return False

def delete_scooter_info(serial_number) -> bool:

    if validate_serial_number(serial_number):
        pass
    else:
        return False
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM scooter_data
        WHERE serial_number = ?
    ''', (serial_number,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False
    conn.close()
    return True

def read_scooter_info(search_param) -> list:
    if len(search_param) < 50:
        pass
    else:
        print("Search parameter is too long. Please enter a shorter term.")
        return []
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    query = '''
        SELECT * FROM scooter_data
        WHERE brand LIKE ?
        OR model LIKE ?
        OR serial_number LIKE ?
        OR CAST(top_speed AS TEXT) LIKE ?
        OR CAST(battery_capacity AS TEXT) LIKE ?
        OR CAST(state_of_charge AS TEXT) LIKE ?
        OR CAST(target_range_soc AS TEXT) LIKE ?
        OR location LIKE ?
        OR CAST(out_of_service AS TEXT) LIKE ?
        OR CAST(mileage AS TEXT) LIKE ?
        OR last_maintenance_date LIKE ?
    '''
    search_term = f"%{search_param}%"
    cursor.execute(query, [search_term] * 11)
    scooters = cursor.fetchall()
    
    conn.close()
    
    if not scooters:
        return []
    
    return scooters