import sqlite3

def create_traveller(firstname, lastname, birthday, gender, streetname, house_number, 
                    zip_code, city, email_address, mobile_phone, driving_license_number):
    conn = sqlite3.connect('../database/urban_mobility.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO travellers (
            first_name, last_name, birthday, gender, street_name, house_number, zip_code, city, email_address, mobile_phone, driving_license_number
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (firstname, lastname, birthday, gender, streetname, house_number, zip_code, city, email_address, mobile_phone, driving_license_number)
        )

    conn.commit()
    conn.close()

    return True
    # Example function call
    # Replace the arguments with actual values as needed
create_traveller(
    "John",
    "Doe",
    "1990-01-01",
    "M",
    "Main Street",
    "123",
    "12345",
    "Sample City",
    "john.doe@example.com",
    "1234567890",
    "DL123456"
)
