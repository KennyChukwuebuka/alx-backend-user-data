#!/usr/bin/env python3
"""DB module

Contains the class DB
    implement the add_user method
    DB._session is a private property NEVER use fromoutside DB class
    implement add_user method which has string
    argument email and hashed_password
    return user object and save user to the database
"""

import logging
from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User

logging.disable(logging.WARNING)


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            print(f"Error adding user to database: {e}")
            self._session.rollback()
            raise
        return user

    def find_user_by(self, **kwargs: dict[str, str]) -> User:
        """Find a user by the given arguments
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).first()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        # print("Type of user: {}".format(type(user)))
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user in the database
        """
        try:
            # Find the user with the given user ID
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError("User with id {} not found".format(user_id))

        # Update user's attributes
        for key, value in kwargs.items():
            if not hasattr(user, key):
                # Raise error if an argument that does not correspond to a user
                # attribute is passed
                raise ValueError("User has no attribute {}".format(key))
            setattr(user, key, value)

        try:
            # Commit changes to the database
            self._session.commit()
        except InvalidRequestError:
            # Raise error if an invalid request is made
            raise ValueError("Invalid request")
