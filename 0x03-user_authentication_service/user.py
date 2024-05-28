#!/usr/bin/env python3
"""
Create an SQLAlchemy model of a User for a Database table users
Model attributes:
    id (integer, primary key, auto-generated by default)
    email (string)
    hashed_password (string)
    session_id (string)
    reset_token (string)
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User model
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str) -> None:
        """ Initializes a new User
        """
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        """ Returns a string representation of the User
        """
        return f"<User {self.email}>"

    def __str__(self) -> str:
        """ Returns a string representation of the User
        """
        return f"<User {self.email}>"

    def __eq__(self, other: object) -> bool:
        """ Returns True if other is equal to self
        """
        if not isinstance(other, User):
            return False
        return self.email == other.email

    def __ne__(self, other: object) -> bool:
        """ Returns True if other is not equal to self
        """
        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool:
        """ Returns True if self is less than other
        """
        if not isinstance(other, User):
            return False
        return self.email < other.email

    def __gt__(self, other: object) -> bool:
        """ Returns True if self is greater than other
        """
        if not isinstance(other, User):
            return False
        return self.email > other.email

    def __hash__(self) -> int:
        """ Returns the hash value of self
        """
        return hash(self.email)

    def display_name(self) -> str:
        """ Display User name based on email/first_name/last_name
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    def is_valid_password(self, pwd: str) -> bool:
        """ Validate a password
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.hashed_password, pwd)
        self.session_id = session_id
