"""Security module."""
from bcrypt import checkpw, gensalt, hashpw


def generate_password_hash(password: "str") -> "str":
    """Generates a pass hash."""
    password_bin: "bytes" = password.encode("utf-8")
    hashed: "bytes" = hashpw(password_bin, gensalt())
    hashed_decoded: "str" = hashed.decode("utf-8")
    return hashed_decoded


def check_password_hash(plain_password: "str", password_hash: "str") -> "bool":
    """Checks the password for legitimacy."""
    plain_password_bin: "bytes" = plain_password.encode("utf-8")
    password_hash_bin: "bytes" = password_hash.encode("utf-8")
    is_correct: "bool" = checkpw(plain_password_bin, password_hash_bin)
    return is_correct
