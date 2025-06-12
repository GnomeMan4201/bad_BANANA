import re
from cryptography.fernet import Fernet

# Load encryption key
with open("encryption_key.key", "rb") as keyfile:
    key = keyfile.read()
cipher = Fernet(key)

# Define regex patterns for common token formats
TOKEN_PATTERNS = [
    r'(?i)bearer\s+([a-zA-Z0-9\-_]+)',  # Bearer tokens
    r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+',  # JWT Tokens
    r'ghp_[a-zA-Z0-9]{36}',  # GitHub Personal Access Tokens
    r'ya29\.[0-9A-Za-z\-_]+',  # Google OAuth Tokens
    r'AKIA[0-9A-Z]{16}',  # AWS Access Key
    r'AIza[0-9A-Za-z\-_]{35}',  # Google API Key
]

# Read token file
with open("realtime_leaked_keys.log", "r") as file:
    lines = file.readlines()

valid_tokens = []
invalid_tokens = []

# Scan each line
for line in lines:
    token_found = None
    for pattern in TOKEN_PATTERNS:
        match = re.search(pattern, line)
        if match:
            token_found = match.group(0)
            break
    
    if token_found:
        print(f"[✅] Valid Token Found: {token_found}")
        valid_tokens.append(token_found)
    else:
        print(f"[❌] Invalid Token: {line.strip()}")
        invalid_tokens.append(line.strip())

# Encrypt valid tokens
with open("secure_tokens.enc", "wb") as enc_file:
    for token in valid_tokens:
        encrypted_token = cipher.encrypt(token.encode())
        enc_file.write(encrypted_token + b"\n")

print(f"\n🔒 Encrypted {len(valid_tokens)} valid tokens.")
print(f"⚠️ Ignored {len(invalid_tokens)} non-token entries.")

