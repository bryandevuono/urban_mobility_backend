import sqlite3
from datetime import datetime
import sys
import string
import random
sys.path.insert(0, './validation')
from account_data import validate_username, validate_password, validate_name
sys.path.insert(0, './auth')
from hash import hash_password, check_password
sys.path.insert(0, './encryption')
from logger import log_event
from symmetric import encrypt_message, decrypt_message

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
            log_event(f"Failed to create user {username}. Validation failed.", "1")
            return False
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    # Check if the username already exists
    cursor.execute('''
        SELECT username FROM users
    ''')

    for row in cursor.fetchall():
        if decrypt_message(row[0]) == username.lower():
            print("\nUsername already exists.")
            conn.close()
            log_event(f"Failed to create user {username}. Username already exists.", "1")
            return False
        
    username = username.lower()
    password = hash_password(password)
    cursor.execute('''
        INSERT INTO users (
            username, password, first_name, last_name, role, register_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (encrypt_message(username), password, firstname, lastname, role, datetime.now())
        )

    conn.commit()

    conn.close()
    log_event(f"User {username} created successfully.", "0")
    return True

def read_users(role) -> list:
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    query = '''
        SELECT id, username, first_name, role, last_name, register_date FROM users
    '''
    if role == "system_admin":
        query += " WHERE role = 'service_engineer'"
    cursor.execute(query)
    users = [list(row) for row in cursor.fetchall()]
    conn.close()
    for user in users:
        # Decrypt the username
        user[1] = decrypt_message(user[1])

    log_event(f"Read users with role {role} successfully.", "0")
    return users

def delete_user(id, role) -> bool:
    # Validate the username and role
    if id and isinstance(id, str) and len(id) < 8:
        pass
    else:
        log_event(f"Failed to delete user with id {id}. Invalid id format.", "1")
        print("\nInvalid Id.")
        return False
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM users
        WHERE id = ? AND role = ?
    ''', ((int(id)), role))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        log_event(f"User with id {id} deleted successfully.", "0")
        return True
    else:
        log_event(f"Failed to delete user with id {id}. No user found with the specified id and role.", "1")
        return False

def modify_password(old_password, password_input, username) -> bool:
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    # Validate the password before proceeding
    cursor.execute('''
        SELECT username, password
        FROM users
    ''')
    users = cursor.fetchall()

    username_db = ""
    password_db = ""
    for user in users:
        if decrypt_message(user[0]) == username:
            username_db = user[0]
            password_db = user[1]

    if check_password(old_password, password_db):
        pass
    else:
        print("\nOld password is incorrect.")
        log_event(f"Failed to modify password for user {username}. Old password is incorrect.", "1")
        return False
    
    if validate_password(password_input):
        pass
    else:
        print("Invalid password format.")
        log_event(f"Failed to modify password for user {username}. Invalid password format.", "1")
        return False
    
    # Check if the new password is the same as the old one
    if password_db == old_password:
        print("\nThe new password cannot be the same as the current password.")
        conn.close()
        log_event(f"Failed to modify password for user {username}. New password is the same as the current password.", "1")
        return False
    
    new_hashed_password = hash_password(password_input)
    # Update the password in the database
    cursor.execute('''
        UPDATE users
        SET password = ?
        WHERE username = ?
    ''', (new_hashed_password, username_db))

    conn.commit()
    conn.close()
    log_event(f"Password for user {username} modified successfully.", "0")
    return True

def update_profile(new_username, firstname, lastname, id, role) -> bool:
    # Validate the inputs of selecting the user to update
    if id and isinstance(id, str) and len(id) < 8:
        pass
    else:
        log_event(f"Failed to update profile for user with id {id}. Invalid id format.", "1")
        print("\nInvalid Id.")
        return False
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    #check if the username exists by decrypting all usernames in the database
    cursor.execute('''
        SELECT username
        FROM users
        WHERE id = ? AND role = ?
    ''', (int(id), role))
    user = cursor.fetchone()
    if user:
        pass
    else:
        log_event(f"Failed to update profile for user with id {id}. No user found with the specified id and role.", "1")
        print("No user found with the specified id and role.")
        conn.close()
        return False

    query = "UPDATE users SET "
    params = []
    if len(firstname) > 0 and validate_name(firstname):
        query += "first_name = ?, "
        params.append(firstname)
    if len(lastname) > 0 and validate_name(lastname):
        query += "last_name = ?, "
        params.append(lastname)
    if len(new_username) > 0 and validate_username(new_username):
        new_username = encrypt_message(new_username.lower())
        query += "username = ?, "
        params.append(new_username)

    if params:
        pass
    else:
        print("\nNo inputs provided for update.")
        conn.close()
        log_event(f"Failed to update profile for user with id {id}. No valid inputs provided.", "1")
        return False
    
    query = query.rstrip(', ') + " WHERE id = ? AND role = ?"
    params.append(int(id))
    params.append(role)
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    log_event(f"Profile for user with id {id} updated successfully.", "0")
    return True

def reset_password(id, role) -> str:
    if id and isinstance(id, str) and len(id) < 8:
        pass
    else:
        print("\nInvalid Id.")
        log_event(f"Failed to reset password for user with id {id}. Invalid id format.", "1")
        return ""
    
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()

    all_characters = string.ascii_letters + string.digits + string.punctuation

    length = 30

    generated_temp_password = ''.join(random.choices(all_characters, k=length))    
    hashed_password = hash_password(generated_temp_password)

    cursor.execute('''
        UPDATE users
        SET password = ?
        WHERE id = ?
        AND role = ?
    ''', (hashed_password, int(id), role))
    
    conn.commit()

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        log_event(f"Password for user with id {id} reset successfully.", "0")
        return "This is your temporary password: " + generated_temp_password + "\nPlease change it after logging in."
    else:
        log_event(f"Failed to reset password for user with id {id}. No user found with the specified id and role.", "1")
        conn.close()
        return "No user found with the specified username and role."