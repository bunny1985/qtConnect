import hashlib, binascii, os


def _hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def _verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


class UserBasicData:
    _email: str
    _password: str

    def __init__(self, email, password):
        self._email = email
        self._password = _hash_password(password)

    def get_password(self) -> str:
        return self._password

    def __str__(self):
        return f"{self._email}:{self._password}"


class AuthenticationManager:
    def get_user_by_email(self, mail: str) -> UserBasicData:
        pass

    def save_user(user_basic_data: UserBasicData):
        pass

    def verify_pass_for_user(self, email: str, passworrd: str):
        user = self.get_user_by_email(email)
        return _verify_password(user.get_password(), passworrd)
