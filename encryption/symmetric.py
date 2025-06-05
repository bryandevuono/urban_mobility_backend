import os
from cryptography.fernet import Fernet

KEY_FILE = "../encryption/secret.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
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