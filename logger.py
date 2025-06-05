import sqlite3

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

def log_event(username, description, suspicious, db_path='logging.db'):
    from datetime import datetime
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    cursor.execute('''
        INSERT INTO logging (date, time, username, description, suspicious)
        VALUES (?, ?, ?, ?, ?)
    ''', (date_str, time_str, username, description, suspicious))
    
    conn.commit()
    conn.close()

def read_logs(db_path='../logging.db') -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logging')
    logs = cursor.fetchall()
    conn.close()
    print("Logging Records:")
    for log in logs:
        print(f"ID: {log[0]}, Date: {log[1]}, Time: {log[2]}, Username: {log[3]}, Description: {log[4]}, Suspicious: {'Yes' if log[5] else 'No'}")

if __name__ == "__main__":
    create_logging_table()
    print("Logging table created (if not exists).")