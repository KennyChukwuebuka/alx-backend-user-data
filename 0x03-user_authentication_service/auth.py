#!/usr/bin/env python3
""" Auth module
"""

import hashlib
import bcrypt
from db import DB
from sqlalchemy.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID.

    Returns:
        str: A string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth class."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password.

        Args:
            email (str): The email address of the user.
            password (str): The plain text password of the user.

        Raises:
            ValueError: If a user with the given email already exists.

        Returns:
            User: The newly created user object.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials.

        Args:
            email (str): The email address of the user.
            password (str): The plain text password of the user.

        Returns:
            bool: True if the login credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for a user.

        Args:
            email (str): The email address of the user.

        Returns:
            str: The session ID for the user, or None if the user is not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.create_session(user.id, session_id)
            return session_id
        except NoResultFound:
            return None
