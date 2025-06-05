import os
from cryptography.fernet import Fernet

KEY_FILE = "./encryption/secret.key"

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

def encrypt_message(message: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.encrypt(message)

def decrypt_message(encrypted_message: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message)

message = b"Hello, this is a secret message!"
encrypted = encrypt_message(message)
print(f"Encrypted message: {encrypted}")
decrypted = decrypt_message(encrypted)
print(f"Decrypted message: {decrypted.decode()}")
# Ensure the decrypted message matches the original
if decrypted == message:
    print("Decryption successful!")