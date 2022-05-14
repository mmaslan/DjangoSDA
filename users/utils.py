import hashlib

def hash_password_without_salt(password: str ) -> str:
    hash_password = hashlib.sha256(password.encode("ASCII")).hexdigest()
    return hash_password

def verification_without_salt(password: str, hash_password: str) -> bool:
    input_password = hashlib.sha256(password.encode("ASCII")).hexdigest()
    return input_password == hash_password