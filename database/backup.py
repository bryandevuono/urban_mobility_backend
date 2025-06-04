import zipfile
import os
import sqlite3
from datetime import datetime, timedelta

# TODO: implement role check for backing up and restoring the database
# TODO: restore database from backup refine

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

def restore_database(backup_filename, restore_code) -> bool:
    if len(backup_filename) > 0 and len(backup_filename) < 40:
        pass
    backup_path = f"./database/backups/{backup_filename}"
    if not os.path.exists(backup_path):
        print(f"Backup file '{backup_filename}' not found.")
        return
    
    with zipfile.ZipFile(backup_path, mode='r') as zf:
        zf.extractall("./database")

    print(f"Database restored from backup: {backup_filename}")
    return True

def create_restore_code(admin_username) -> str:
    if len(admin_username) > 0 and len(admin_username) < 20:
        pass
    else:
        print("Username must be between 1 and 20 characters long.")
        return ""
    #check if user exists and is an admin
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ?", (admin_username,))
    role = cursor.fetchone()
    cursor.execute("SELECT * FROM backup_codes WHERE username = ?", (admin_username,))
     # check if the user already has a code
    code_count = len(cursor.fetchall())
    if role[0] == 'system_admin' and code_count == 0:
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
        print("User is not found or already has a code.")
        conn.close()
        return ""

def revoke_restore_code(username) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM backup_codes WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("UPDATE backup_codes SET used = TRUE WHERE code = ?", (username,))
        conn.commit()
        print("Restore code revoked successfully.")
        return True
    else:
        print("Restore code not found.")
        return False
    
def check_restore_code(restore_code) -> bool:
    if len(restore_code) > 0 and len(restore_code) < 40:
        pass
    else:
        print("Restore code must be between 1 and 40 characters long.")
        return False
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM backup_codes WHERE code = ? AND used = ?", (restore_code, False))
    result = cursor.fetchone()
    expiration_date = datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S.%f')

    if result and datetime.now() > expiration_date:
        cursor.execute("UPDATE backup_codes SET used = ? WHERE code = ?", (True, restore_code))
        print("Restore code is valid.")
        return True
    elif datetime.now() > expiration_date:
        print("Restore code has expired.")
        return False
    else:
        print("Invalid or already used restore code.")
        return False
    
