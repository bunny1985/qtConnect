from bcrypt import hashpw, gensalt, checkpw

from infrastructure.redis import db

from typing import Optional


def _hash_password(password):
    """Hash a password for storing."""
    if type(password) is str:
        password = password.encode('utf-8')
    return hashpw(password, gensalt())


def _verify_password(stored_password_hash, provided_password):
    """Verify a stored password against one provided by user"""
    return checkpw(provided_password.encode('utf-8'), stored_password_hash.encode('utf-8'))


class UserBasicData:
    _email: str
    _password: str

    def __init__(self, email, password, hash_password=True):
        """Remember - when retriving from database you have a password hash already - so dont hash it one more time"""
        self._email = email
        if hash_password:
            self._password = _hash_password(password)
        else:
            self._password = password

    def get_password(self) -> str:
        return self._password

    def get_mail(self) -> str:
        return self._email

    def __str__(self):
        return f"{self._email}:{self._password}"

    def to_ditctionary(self):
        return {"user_id": self._email, "email": self._email, "password": self._password}


class AuthenticationManager:
    def get_user_by_email(self, mail: str) -> Optional[UserBasicData]:
        key = f"users:{mail}"
        # noinspection PyUnresolvedReferences
        if not db.exists(key):
            return None

        u = db.Hash(key)

        return UserBasicData(u["email"], u["password"], hash_password=False)

    def save_user(self, user_basic_data: UserBasicData):
        u = db.Hash(f"users:{user_basic_data.get_mail()}")
        u.update(user_basic_data.to_ditctionary())

    def verify_pass_for_user(self, email: str, passworrd: str):
        user = self.get_user_by_email(email)
        return _verify_password(user.get_password(), passworrd)
