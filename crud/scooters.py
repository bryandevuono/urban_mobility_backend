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
                        location,out_of_service,mileage,last_maintenance_date) -> bool:
    # check if serial number exists
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
        
    cursor.execute('''
        UPDATE scooter_data
        SET brand = ?,
            model = ?,
            top_speed = ?,
            battery_capacity = ?,
            state_of_charge = ?,
            target_range_soc = ?,
            location = ?,
            out_of_service = ?,
            mileage = ?,
            last_maintenance_date = ?
        WHERE serial_number = ?
    ''', (brand, model, float(top_speed), float(battery_capacity), int(soc), int(target_range_soc), float(location),
          int(out_of_service), float(mileage), last_maintenance_date, serial_number))
    
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False
    conn.close()
    return True

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