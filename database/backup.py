import zipfile
import os
import sqlite3
from datetime import datetime, timedelta

# TODO: implement role check for checking the code
def backup_database() -> bool:
    db_path = "database/urban_mobility.db"
    if not os.path.exists(db_path):
        print(f"Database file '{db_path}' not found.")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_filename = f"{timestamp}_backup.zip"
    with zipfile.ZipFile("./database/backups/" + backup_filename, mode='w') as zf:
        zf.write("./database")

    print(f"Backup created: {backup_filename}")
    return True

def restore_database(backup_filename) -> bool:
    backup_path = f"./database/backups/{backup_filename}"
    if not os.path.exists(backup_path):
        print(f"Backup file '{backup_filename}' not found.")
        return
    
    with zipfile.ZipFile(backup_path, mode='r') as zf:
        zf.extractall("./database")

    print(f"Database restored from backup: {backup_filename}")
    return True

def create_restore_code(admin_username) -> str:
    #check if user exists and is an admin
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ?", (admin_username,))
    result = cursor.fetchone()
    if result[0] == 'system_admin':
        #genetate a restore code
        restore_code = os.urandom(16).hex()
        expiration_date = datetime.now() + timedelta(days=1) 
        #place it in the database
        cursor.execute("INSERT INTO backup_codes (code, username, used, expiration_date, created_at) VALUES (?, ?, ?, ?, ?)", 
                       (restore_code, admin_username, False, expiration_date, datetime.now()))
        #display the restore code
        conn.commit()
        conn.close()
        return restore_code
    else:
        print("User is not found.")
        conn.close()
        return ""

def revoke_restore_code(restore_code) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM backup_codes WHERE code = ?", (restore_code,))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("UPDATE backup_codes SET used = TRUE WHERE code = ?", (restore_code,))
        conn.commit()
        print("Restore code revoked successfully.")
        return True
    else:
        print("Restore code not found.")
        return False
    
def check_restore_code(restore_code) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM backup_codes WHERE code = ? AND used = ?", (restore_code, False))
    result = cursor.fetchone()
    
    if result:
        # Check if the code is expired
        expiration_date = datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S.%f')
        if datetime.now() > expiration_date:
            print("Restore code has expired.")
            return False
        else:
            # Mark the code as used
            cursor.execute("UPDATE backup_codes SET used = ? WHERE code = ?", (True, restore_code))
            print("Restore code is valid.")
            return True
    else:
        print("Invalid or already used restore code.")
        return False
    
