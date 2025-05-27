import sqlite3

def add_service_engineer(username, password, firstname, lastname, role, register_date):
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (
            username, password, firstname, lastname, role, register_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password, firstname, lastname, role, register_date)
        )

    conn.commit()
    conn.close()

    return True
