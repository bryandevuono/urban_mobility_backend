import sqlite3
import sys
sys.path.insert(0, '../validation')
from traveller_data import validate_name, validate_gender, validate_birthday, validate_house_number, validate_zip_code, validate_city, validate_email, validate_phone_number_nl, validate_driver_license_number
sys.path.insert(0, '../encryption')
from symmetric import encrypt_message, decrypt_message

def create_traveller(firstname, lastname, birthday, gender, streetname, house_number, 
                    zip_code, city, email_address, mobile_phone, driving_license_number)-> bool:
    validators = [
        validate_name(firstname),
        validate_name(lastname),
        validate_gender(gender),
        validate_name(streetname),
        validate_birthday(birthday),
        validate_house_number(house_number),
        validate_zip_code(zip_code),
        validate_city(city),
        validate_email(email_address),
        validate_phone_number_nl(mobile_phone),
        validate_driver_license_number(driving_license_number)
    ]

    for validator in validators:
        if validator:
            pass
        else:
            return False
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO travellers (
            first_name, last_name, birthday, gender, street_name, house_number, zip_code, city, email_address, mobile_phone, driving_license_number
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (firstname, lastname, birthday, gender, encrypt_message(streetname), house_number, zip_code, city, email_address, encrypt_message(mobile_phone), driving_license_number)
        )

    conn.commit()
    conn.close()

    return True

def remove_traveller(traveller_email) -> bool:
    if validate_email(traveller_email):
        pass
    else:
        print("Invalid email address.")
        return False
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM travellers WHERE email_address = ?
        ''', (traveller_email,))

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return True
    else:
        return False

def read_traveller(search_param) -> str:
    #buffer overflow protection
    if len(search_param) > 60:
        return "Search term too long."
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
    validators = [
        validate_name(first_name),
        validate_name(last_name),
        validate_gender(gender),
        validate_name(streetname),
        validate_birthday(birth_date),
        validate_house_number(house_number),
        validate_zip_code(zip_code),
        validate_city(city),
        validate_email(email_address),
        validate_phone_number_nl(phone_number),
        validate_driver_license_number(driving_license_number)
    ]

    for validator in validators:
        if validator:
            pass
        else:
            return False
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