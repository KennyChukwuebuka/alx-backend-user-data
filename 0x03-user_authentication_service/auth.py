#!/usr/bin/env python3
""" Auth module
"""

import hashlib
import bcrypt
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hash password
    Note: the returned bytes should be a salted hash of the input password
    hashed with bycrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize the Auth class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> str:
        """Register a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))
            return True
