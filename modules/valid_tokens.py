import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.exceptions import InvalidTag
import base64

def encrypt_token(token, key, iv):
    """Encrypts a single token using AES-256 in GCM mode (Authenticated Encryption)."""
    if len(key) not in (16, 24, 32):
        raise ValueError("Key must be 16, 24, or 32 bytes long (128, 192, or 256 bits).")
    if len(iv) != 12:  # GCM mode uses 12-byte IV (96 bits)
        raise ValueError("IV must be 12 bytes long for AES-GCM.")

    # AES-GCM doesn't require padding, so we can directly encode the token
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(token.encode()) + encryptor.finalize()

    # The GCM mode also generates an authentication tag
    return base64.b64encode(ciphertext).decode(), base64.b64encode(encryptor.tag).decode()

def decrypt_token(encrypted_token, tag, key, iv):
    """Decrypts a single token using AES-256 in GCM mode (Authenticated Decryption)."""
    if len(key) not in (16, 24, 32):
        raise ValueError("Key must be 16, 24, or 32 bytes long (128, 192, or 256 bits).")
    if len(iv) != 12:
        raise ValueError("IV must be 12 bytes long for AES-GCM.")

    ciphertext = base64.b64decode(encrypted_token)
    tag = base64.b64decode(tag)
    
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    try:
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    except InvalidTag:
        raise ValueError("Decryption failed. Incorrect key, IV, or corrupted data.")

    return decrypted_data.decode()

def save_encrypted_tokens(tokens, file_path, key, iv):
    """Encrypts a list of tokens and saves them to a file, along with the key, IV, and tags."""
    with open(file_path, "w") as f:
        f.write(base64.b64encode(key).decode() + "\n")  # Key on first line
        f.write(base64.b64encode(iv).decode() + "\n")   # IV on second line
        for token in tokens:
            encrypted_token, tag = encrypt_token(token, key, iv)
            f.write(encrypted_token + "\n")
            f.write(tag + "\n")

def load_encrypted_tokens(file_path):
    """Loads and decrypts tokens from a file. Returns the list of decrypted tokens."""
    decrypted_tokens = []
    with open(file_path, "r") as f:
        key = base64.b64decode(f.readline().strip())  # Read key from first line
        iv = base64.b64decode(f.readline().strip())   # Read IV from second line
        for line in f:
            encrypted_token = line.strip()
            tag = f.readline().strip()
            try:
                decrypted_tokens.append(decrypt_token(encrypted_token, tag, key, iv))
            except ValueError as e:
                print(f"Error decrypting token: {e}")
    return decrypted_tokens

def main():
    """Example usage: Encrypts some tokens, saves them, then loads and decrypts them."""
    # --- Encryption Example ---
    tokens = ["token1", "token2", "supersecrettoken3"]
    file_path = "encrypted_tokens_gcm.txt"

    # Generate a new key and IV securely
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(12)   # 12-byte IV (96 bits for GCM)

    save_encrypted_tokens(tokens, file_path, key, iv)
    print(f"Tokens encrypted and saved to {file_path}")

    # --- Decryption Example ---
    try:
        decrypted_tokens = load_encrypted_tokens(file_path)
        print("Decrypted tokens:", decrypted_tokens)
    except ValueError as e:
        print(f"Error decrypting tokens: {e}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

if __name__ == "__main__":
    main()
