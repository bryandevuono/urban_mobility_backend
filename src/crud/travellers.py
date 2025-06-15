import sqlite3
import sys
sys.path.insert(0, './validation')
from traveller_data import validate_name, validate_gender, validate_birthday, validate_house_number, validate_zip_code, validate_city, validate_email, validate_phone_number_nl, validate_driver_license_number
sys.path.insert(0, './encryption')
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
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO travellers (
                first_name, last_name, birthday, gender, street_name, house_number, zip_code, city, email_address, mobile_phone, driving_license_number
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (firstname, lastname, birthday, gender, encrypt_message(streetname), house_number, zip_code, city, email_address, encrypt_message(mobile_phone), driving_license_number)
            )
    except sqlite3.IntegrityError as e:
        print(f"Error adding traveller, possibly due to duplicate email address, check your input")
        conn.close()
        return False
    conn.commit()
    conn.close()

    return True

def remove_traveller(traveller_email) -> bool:
    if validate_email(traveller_email):
        pass
    else:
        print("\nInvalid email address.")
        return False
    conn = sqlite3.connect('./database/urban_mobility.db')
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

def read_traveller(search_param) -> None:
    #buffer overflow protection
    if len(search_param) > 60:
        return "Search term too long."
    conn = sqlite3.connect('./database/urban_mobility.db')
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
    
    if travellers:
        print("\nTraveller found:")
        print("========================================")
        for i, column in enumerate(cursor.description):
            if column[0] == 'mobile_phone' or column[0] == 'street_name':
                print(f"{column[0]}: {decrypt_message(travellers[i])}")
            else:
                print(f"{column[0]}: {travellers[i]}")
    else:
        print("No traveller found with the specified search term.")
        return None

def update_traveller(email_to_search, email_address,first_name,last_name,birth_date,phone_number,gender,
                     streetname,house_number,zip_code,city,driving_license_number) -> bool:
    if validate_email(email_to_search):
        pass
    else:
        print("\nInvalid email address.")
        return False
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    query = "UPDATE travellers SET "
    params = []
    if email_address and validate_email(email_address):
        query += ", email_address = ?"
        params.append(email_address)
    if first_name and validate_name(first_name):
        query += ", first_name = ?"
        params.append(first_name)
    if last_name and validate_name(last_name):
        query += ", last_name = ? "
        params.append(last_name)
    if birth_date and validate_birthday(birth_date):
        query += ", birthday = ?"
        params.append(birth_date)
    if phone_number and validate_phone_number_nl(phone_number):
        query += ", mobile_phone = ?"
        params.append(encrypt_message(phone_number))
    if gender and validate_gender(gender):
        query += ", gender = ?"
        params.append(gender)
    if streetname and validate_name(streetname):
        query += ", street_name = ?"
        params.append(encrypt_message(streetname))
    if house_number and validate_house_number(house_number):
        query += ", house_number = ?"
        params.append(house_number)
    if zip_code and validate_zip_code(zip_code):
        query += ", zip_code = ?"
        params.append(zip_code)
    if city and validate_city(city):
        query += ", city = ?"
        params.append(city)
    if driving_license_number and validate_driver_license_number(driving_license_number):
        query += ", driving_license_number = ?"
        params.append(driving_license_number)

    if params:
        pass
    else:
        print("\nNo inputs provided for update.")
        conn.close()
        return False
    
    query = query.replace(", ", " ", 1)
    query += " WHERE email_address = ?"
    params.append(email_to_search)
    cursor.execute(query, params)
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        print("No traveller found with the specified email address.")
        return False
    conn.close()
    return True