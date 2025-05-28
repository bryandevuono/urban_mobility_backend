import sqlite3

def create_traveller():
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO travellers (
            
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password, firstname, lastname, role, datetime.now())
        )

    conn.commit()
    conn.close()

    return True