from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def generate_key():
    return get_random_bytes(32)