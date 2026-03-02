import secrets

def security_key():
    security_key =secrets.token_hex(16)
    return security_key