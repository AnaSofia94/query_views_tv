import secrets

def generate_api_key():
    return secrets.token_hex(32)

api_key = generate_api_key()

print(f"Generated API Key: {api_key}")