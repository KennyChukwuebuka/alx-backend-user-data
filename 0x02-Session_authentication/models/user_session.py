#!/usr/bin/env python3
""" User session module
"""

from sqlalchemy import Column, String
from .base import Base


class UserSession(Base):
    __tablename__ = 'user_session'

    user_id = Column(String, primary_key=True)
    session_id = Column(String)

    def __init__(self, user_id: str, session_id: str,
                 *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.session_id = session_id
