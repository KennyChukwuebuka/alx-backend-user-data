#!/usr/bin/env python3
"""DB module

Contains the class DB
    implement the add_user method
    DB._session is a private property NEVER use fromoutside DB class
    implement add_user method which has string
    argument email and hashed_password
    return user object and save user to the database
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


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
        """add_user method
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def get_user(self, email: str) -> User:
        """get_user method
        """
        return self._session.query(User).filter(User.email == email).first()

    def destroy_session(self, user_id: int) -> None:
        """destroy_session method
        """
        user = self._session.query(User).filter(User.id == user_id).first()
        if user:
            user.session_id = None
            self._session.commit()

    def update_session(self, user_id: int, session_id: str) -> None:
        """update_session method
        """
        user = self._session.query(User).filter(User.id == user_id).first()
        if user:
            user.session_id = session_id
            self._session.commit()

    def get_reset_password_token(self, email: str) -> str:
        """get_reset_password_token method
        """
        user = self._session.query(User).filter(User.email == email).first()
        if user:
            return user.reset_token
        return None
