import sqlite3

def add_scooter(brand, model, serial_number, top_speed,battery_capacity, soc, target_range_soc_min, target_range_soc_max,
                latitute, longitude, out_of_service, mileage, last_maintenance_date) -> bool:
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()

    # Insert the new scooter into the database
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

    print("Scooter added successfully!")

add_scooter(
    "Xiaomi", "M365", "SN123456dsdsad", 25, 7800, 90, 20, 80, 52.5200, 13.4050, 0, 1200, "2024-06-01"
)