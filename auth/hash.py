import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, stored_hash):
    # stored_hash is from the db
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)