import zipfile
import os
from datetime import datetime

def backup_database():
    db_path = "database/urban_mobility.db"
    if not os.path.exists(db_path):
        print(f"Database file '{db_path}' not found.")
        return
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{timestamp}_backup.zip"
    with zipfile.ZipFile("./database/backups/" + backup_filename, mode='w') as zf:
        zf.write("./database")
    print(f"Backup created: {backup_filename}")

def restore_database(backup_filename):
    backup_path = f"./database/backups/{backup_filename}"
    if not os.path.exists(backup_path):
        print(f"Backup file '{backup_filename}' not found.")
        return
    with zipfile.ZipFile(backup_path, mode='r') as zf:
        zf.extractall("./database")
    print(f"Database restored from backup: {backup_filename}")