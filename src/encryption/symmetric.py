import os
from cryptography.fernet import Fernet

key_file = "./encryption/secret.key"

def load_or_create_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        with open(key_file, "rb") as f:
            key = f.read()
    return key

key = load_or_create_key()

def encrypt_message(message: str) -> bytes:
    cipher = Fernet(key)
    return cipher.encrypt(message.encode("utf-8"))

def decrypt_message(encrypted_message) -> str:
    cipher = Fernet(key)
    decrypted_bytes = cipher.decrypt(encrypted_message)
    return decrypted_bytes.decode("utf-8")