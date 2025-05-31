import sqlite3

def create_traveller(firstname, lastname, birthday, gender, streetname, house_number, 
                    zip_code, city, email_address, mobile_phone, driving_license_number)-> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO travellers (
            first_name, last_name, birthday, gender, street_name, house_number, zip_code, city, email_address, mobile_phone, driving_license_number
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (firstname, lastname, birthday, gender, streetname, house_number, zip_code, city, email_address, mobile_phone, driving_license_number)
        )

    conn.commit()
    conn.close()

    return True

def remove_traveller(traveller_email) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM travellers WHERE email_address = ?
        ''', (traveller_email,))

    conn.commit()
    conn.close()

    return True

def read_traveller(search_param) -> str:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    query = '''
        SELECT * FROM travellers
        WHERE first_name LIKE ?
        OR last_name LIKE ?
        OR house_number LIKE ?
        OR city LIKE ?
        OR email_address LIKE ?
        OR birthday LIKE ?
        OR gender LIKE ?
        OR street_name LIKE ?
        OR house_number LIKE ?
        OR zip_code LIKE ?
        OR mobile_phone LIKE ?
        OR driving_license_number LIKE ?
    '''
    search_term = f"%{search_param}%"
    cursor.execute(query, [search_term] * 12)
    travellers = cursor.fetchone()
    
    conn.close()
    
    if not travellers:
        return "Traveller not found."
    
    return travellers

def update_traveller(email_to_search, email_address,first_name,last_name,birth_date,phone_number,gender,
                     streetname,house_number,zip_code,city,driving_license_number) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE travellers
        SET email_address = ?,
            first_name = ?, 
            last_name = ?, 
            birthday = ?,
            gender = ?,
            street_name = ?,
            house_number = ?,
            zip_code = ?,
            city = ?,
            mobile_phone = ?,
            driving_license_number = ?
        WHERE email_address = ?
    ''', (email_address,first_name,last_name,birth_date,phone_number,gender,
        streetname,house_number,zip_code,city,driving_license_number, email_to_search))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated