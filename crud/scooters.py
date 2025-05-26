import sqlite3

errors = []

def add_scooter_info(brand, model, serial_number, top_speed,battery_capacity, soc, target_range_soc_min, target_range_soc_max,
                latitute, longitude, out_of_service, mileage, last_maintenance_date) -> bool:
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO scooter_data (
            brand, model, serial_number, top_speed, battery_capacity, state_of_charge,
            target_range_soc_min, target_range_soc_max, latitude, longitude,
            out_of_service, mileage, last_maintenance_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (brand,model,serial_number,top_speed,battery_capacity,soc,target_range_soc_min,target_range_soc_max,latitute,
              longitude,out_of_service,mileage,last_maintenance_date
    ))

    conn.commit()
    conn.close()

    return True

def update_scooter_info( serial_number, brand, model, top_speed, battery_capacity, soc,
                   target_range_soc_min, target_range_soc_max, latitude, longitude,
                   out_of_service, mileage, last_maintenance_date) -> bool:
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE scooter_data
        SET brand = ?,
            model = ?,
            top_speed = ?,
            battery_capacity = ?,
            state_of_charge = ?,
            target_range_soc_min = ?,
            target_range_soc_max = ?,
            latitude = ?,
            longitude = ?,
            out_of_service = ?,
            mileage = ?,
            last_maintenance_date = ?
        WHERE serial_number = ?
    ''', (brand, model, top_speed, battery_capacity, soc, target_range_soc_min, target_range_soc_max,
          latitude, longitude, out_of_service, mileage, last_maintenance_date, serial_number))
    conn.commit()
    if cursor.rowcount == 0:
        errors.append("No scooter found with the given serial number.")
        conn.close()
        return False
    conn.close()
    return True

def delete_scooter_info(serial_number) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM scooter_data
        WHERE serial_number = ?
    ''', (serial_number,))
    conn.commit()
    if cursor.rowcount == 0:
        errors.append("No scooter found with the given serial number.")
        conn.close()
        return False
    conn.close()
    return True