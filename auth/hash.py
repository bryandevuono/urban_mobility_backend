import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, stored_hash):
    # Ensure password is bytes
    if isinstance(password, str):
        password = password.encode('utf-8')
    # Ensure stored_hash is bytes
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')
    return bcrypt.checkpw(password, stored_hash)