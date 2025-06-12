from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b"ThisIsA32ByteKeyForAES256Crypto!!"

def encrypt_payload(data: bytes) -> str:
    nonce = get_random_bytes(12)
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return base64.urlsafe_b64encode(nonce + tag + ciphertext).decode()

def decrypt_payload(encoded: str) -> bytes:
    raw = base64.urlsafe_b64decode(encoded)
    nonce, tag, ciphertext = raw[:12], raw[12:28], raw[28:]
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
