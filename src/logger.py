import sqlite3
from encryption.symmetric import encrypt_message, decrypt_message

def create_logging_table(db_path='logging.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logging (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            username TEXT NOT NULL,
            description TEXT NOT NULL,
            suspicious INTEGER NOT NULL CHECK (suspicious IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

def log_event(username, description, suspicious, db_path='../logging.db'):
    from datetime import datetime
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    cursor.execute('''
        INSERT INTO logging (date, time, username, description, suspicious)
        VALUES (?, ?, ?, ?, ?)
    ''', (encrypt_message(date_str), encrypt_message(time_str), encrypt_message(username), encrypt_message(description), encrypt_message(suspicious)))
    
    conn.commit()
    conn.close()

def read_logs(db_path='../logging.db') -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logging')
    logs = cursor.fetchall()
    conn.close()
    print("Logging Records:")
    print("ID | Date | Time | Username | Description | Suspicious")
    log_counter = 0
    for log in logs:
        print(f"ID: {log[0]}, Date: {decrypt_message(log[1])},Time: {decrypt_message(log[2])}, Username: {decrypt_message(log[3])}, Description: {decrypt_message(log[4])}, Suspicious: {'Yes' if decrypt_message(log[5]) == "1" else 'No'}")
        log_counter += 1
    