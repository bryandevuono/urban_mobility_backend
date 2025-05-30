import sqlite3
from datetime import datetime
import sys
sys.path.insert(0, '../auth')
from hash import hash_password

def create_user(username, password, firstname, lastname, role) -> bool:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()
    
    password = hash_password(password)

    cursor.execute('''
        INSERT INTO users (
            username, password, first_name, last_name, role, register_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password, firstname, lastname, role, datetime.now())
        )

    conn.commit()
    conn.close()

    return True

def read_users() -> list:
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    query = '''
        SELECT * FROM users
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