import zipfile
import os
import sqlite3
from datetime import datetime, timedelta
import sys
sys.path.insert(0, './encryption')
from logger import log_event
from symmetric import encrypt_message, decrypt_message
import re

def backup_database() -> bool:
    db_path = "./database/urban_mobility.db"
    backup_dir = "./database/backups"

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{timestamp}_backup.zip"
    backup_zip_path = os.path.join(backup_dir, backup_filename)
    with zipfile.ZipFile(backup_zip_path, mode='w') as zf:
        zf.write(db_path, arcname=os.path.basename(db_path))

    print(f"\nBackup created: {backup_filename}")
    log_event(f"Backup created: {backup_filename}", "0")
    return True

def restore_database(backup_filename, restore_code, admin_username, role) -> bool:
    if validate_backup_input(backup_filename):
        pass
    else:
        print("Backup filename must be between 1 and 40 characters long.")
        log_event("Backup filename is invalid", "1")
        return False
    
    if role == "super_admin" or len(restore_code) < 50:
        pass
    else:
        print("Restore code must be less than 50 characters long.")
        log_event("Restore code is invalid", "1")
        return False
    
    if len(admin_username) > 0 and len(admin_username) < 12:
        pass
    else:
        log_event("Admin username is invalid (restoring backup)", "1")
        print("Username must be between 1 and 12 characters long.")
        return False
    
    backup_dir = "./database/backups"
    backup_path = os.path.join(backup_dir, backup_filename)
    if not os.path.isfile(backup_path):
        print("\nBackup file not found.")
        return False
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    # check if the user is connected (decrypt the username)
    cursor.execute("SELECT username, id FROM backup_codes")
    users = cursor.fetchall()
    id_username = None
    for user in users:
        if decrypt_message(user[0]) == admin_username:
            id_username = user[1]
            break
    cursor.execute("SELECT * FROM backup_codes WHERE code = ? AND used = ? AND id = ? and expiration_date > DATETIME('now')", 
                   (restore_code, False, id_username))
    
    check_restore_code = cursor.fetchone()

    if admin_username == "super_admin" or check_restore_code:
        with zipfile.ZipFile(backup_path, 'r') as zipf:
            zipf.extract('urban_mobility.db', path='../database')

        print(f"Backup {backup_filename} restored.")
        #mark the restore code as used
        cursor.execute("UPDATE backup_codes SET used = TRUE WHERE code = ?", (restore_code,))
        conn.commit()
        conn.close()

        return True
    else:
        print("Invalid or already used restore code.")
        conn.close()
        log_event("Invalid or already used restore code", "1")
        return False

def create_restore_code(admin_username) -> str:
    if len(admin_username) > 0 and len(admin_username) < 12:
        pass
    else:
        print("Username must be between 1 and 12 characters long.")
        return ""
    #check if user exists and is an admin
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute("SELECT role, username FROM users")
    # decrypt the usernames
    users = cursor.fetchall()
    username = ""
    role = ""
    for user in users:
        if decrypt_message(user[1]) == admin_username:
            username = decrypt_message(user[1])
            role = user[0]
            break
     # check if the user already has a code
    cursor.execute("SELECT COUNT(*) FROM backup_codes WHERE username = ? AND used = ?", (admin_username, False))
    code_count = cursor.fetchone()[0]
    if username and role == 'system_admin' and code_count == 0:
        #genetate a restore code
        restore_code = os.urandom(16).hex()
        expiration_date = datetime.now() + timedelta(days=1) # make the code valid for 1 day
        #place it in the database
        cursor.execute("INSERT INTO backup_codes (code, username, used, expiration_date, created_at) VALUES (?, ?, ?, ?, ?)", 
                       (restore_code, encrypt_message(admin_username), False, expiration_date, datetime.now()))
        #display the restore code
        conn.commit()
        conn.close()
        return restore_code
    else:
        print("\nUser is not found or already has a (used)code.")
        log_event("User is not found or already has a (used) code", "1")
        conn.close()
        return ""

def revoke_restore_code(username) -> bool:
    if len(username) > 0 and len(username) < 11:
        pass
    else:
        print("Username must be between 1 and 12 characters long.")
        return False
    conn = sqlite3.connect('./database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT username, id FROM backup_codes")
    users = cursor.fetchall()
    for user in users:
        if decrypt_message(user[0]) == username:
            id = user[1]
            break
    
    if id:
        cursor.execute("UPDATE backup_codes SET used = TRUE WHERE id = ?", (id,))
        conn.commit()
        print("Restore code revoked successfully.")
        return True
    else:
        print("Restore code not found.")
        return False
    
def validate_backup_input(backup_filename: str) -> bool:
    #no special characters
    pattern = r"^[a-zA-Z0-9_.-]{1,40}$"
    if re.match(pattern, backup_filename) and 1 <= len(backup_filename) <= 40:
        return True
    else:
        print("Backup filename must be between 1 and 40 characters long.")
        return False