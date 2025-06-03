import sqlite3
from datetime import datetime
import sys
import string
import random
sys.path.insert(0, '../validation')
from account_data import validate_username, validate_password, validate_name
sys.path.insert(0, '../auth')
from hash import hash_password, check_password

def create_user(username, password, firstname, lastname, role) -> bool:
    validators = [
        validate_username(username),
        validate_password(password),
        validate_name(firstname),
        validate_name(lastname)
    ]
    
    for validator in validators:
        if validator:
            pass
        else:
            return False
    
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    username = username.lower()
    password = hash_password(password)
    try:
        cursor.execute('''
            INSERT INTO users (
                username, password, first_name, last_name, role, register_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, password, firstname, lastname, role, datetime.now())
            )

        conn.commit()

    except sqlite3.IntegrityError as e:
        print("Error: User with this username already exists.")
    conn.close()

    return True

def read_users() -> list:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    query = '''
        SELECT id, username, first_name, role, last_name, register_date FROM users
    '''
    cursor.execute(query)
    users = cursor.fetchall()
    
    conn.close()
    
    return users

def delete_user(username, role) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM users
        WHERE username = ? AND role = ?
    ''', (username, role))

    conn.commit()
    conn.close()

    return True

def modify_password(old_password, password_input, username) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    # Validate the password before proceeding
    cursor.execute('''
        SELECT password FROM users
        WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()

    if check_password(old_password, result[0]):
        pass
    else:
        print("Old password is incorrect.")
        return False
    
    if not validate_password(password_input):
        return False
    
    # Check if the new password is the same as the old one
    if old_password == password_input:
        print("The new password cannot be the same as the current password.")
        conn.close()
        return False
    
    new_hashed_password = hash_password(password_input)
    # Update the password in the database
    cursor.execute('''
        UPDATE users
        SET password = ?
        WHERE username = ?
    ''', (new_hashed_password, username))

    conn.commit()
    conn.close()
    return True

def update_profile_service_engineer(username, firstname, lastname, user_to_modify):
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users
        SET username = ?,
            first_name = ?,
            last_name = ?
        WHERE username = ?
        AND role = "service_engineer"
    ''', (username, firstname, lastname, user_to_modify))

    conn.commit()
    conn.close()
    return True

def update_profile_admin(username, firstname, lastname, user_to_modify):
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users
        SET username = ?,
            first_name = ?,
            last_name = ?
        WHERE username = ?
        AND role = "system_admin"
    ''', (username, firstname, lastname, user_to_modify))

    conn.commit()
    conn.close()
    return True

def reset_password(username, role) -> str:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    all_characters = string.ascii_letters + string.digits + string.punctuation

    # ask the user for the desired length of the password
    length = 30

    # generate a password using randomly chosen characters
    # using the 'choices' function from the random module
    # and joining the resulting characters into a string
    generated_temp_password = ''.join(random.choices(all_characters, k=length))    
    hashed_password = hash_password(generated_temp_password)

    cursor.execute('''
        UPDATE users
        SET password = ?
        WHERE username = ?
        AND role = ?
    ''', (hashed_password, username, role))

    conn.commit()
    conn.close()
    
    return "This is your temporary password: " + generated_temp_password + "\nPlease change it after logging in."