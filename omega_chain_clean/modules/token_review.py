import json
import os
import base64
import requests
from cryptography.fernet import Fernet

# Configuration
SECURE_TOKEN_FILE = "secure_tokens.enc"
VALID_TOKEN_FILE = "valid_tokens.enc"
TOKEN_VALIDATION_URL = "https://api.example.com/auth/validate"  # Replace with actual API endpoint
ENCRYPTION_KEY = os.getenv("TOKEN_ENCRYPTION_KEY")  # Ensure this is securely stored

def decrypt_tokens(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data)

def validate_token(token):
    """Validates token by making an API request."""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(TOKEN_VALIDATION_URL, headers=headers, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def filter_valid_tokens(tokens):
    valid_tokens = [token for token in tokens if validate_token(token)]
    return valid_tokens

def encrypt_tokens(tokens, file_path, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(json.dumps(tokens).encode())
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def main():
    if not ENCRYPTION_KEY:
        raise ValueError("Encryption key is missing. Set TOKEN_ENCRYPTION_KEY in the environment.")
    
    key = base64.urlsafe_b64encode(ENCRYPTION_KEY.encode()) if len(ENCRYPTION_KEY) != 44 else ENCRYPTION_KEY.encode()
    
    print("Decrypting tokens...")
    tokens = decrypt_tokens(SECURE_TOKEN_FILE, key)
    
    print("Validating tokens...")
    valid_tokens = filter_valid_tokens(tokens)
    
    print(f"Valid tokens found: {len(valid_tokens)}")
    
    print("Re-encrypting valid tokens...")
    encrypt_tokens(valid_tokens, VALID_TOKEN_FILE, key)
    
    print("Process completed. Valid tokens securely stored.")

if __name__ == "__main__":
    main()
