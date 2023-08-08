from cryptography.fernet import Fernet
from django.conf import settings
import base64
import os

class URLEncrypter:
    @staticmethod
    def generate_secret_key():
        # Generate a random 32-byte key
        key = Fernet.generate_key()

        # Encode the key using url-safe base64 encoding
        encoded_key = base64.urlsafe_b64encode(key)

        return encoded_key.decode()

    @staticmethod
    def encrypt(pk):
        secret_key = URLEncrypter.generate_secret_key()
        cipher_suite = Fernet(secret_key.encode())
        data = str(pk).encode()
        encrypted_data = cipher_suite.encrypt(data)
        return encrypted_data.decode(), secret_key

    @staticmethod
    def decrypt(encrypted_data, secret_key):
        cipher_suite = Fernet(secret_key.encode())
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
        pk = int(decrypted_data.decode())
        return pk
