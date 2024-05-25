#!/usr/bin/env python3
""" User session module
"""

# models/user_session.py
from models.base import Base
import json
import os


class UserSession(Base):
    """ UserSession model to manage user sessions """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a new UserSession instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')

    def save(self):
        """ Save the session to the file database """
        file_path = 'user_sessions.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data.append(self.to_dict())
        with open(file_path, 'w') as f:
            json.dump(data, f)

    @classmethod
    def find_by_session_id(cls, session_id):
        """ Find a session by session_id """
        file_path = 'user_sessions.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                for session in data:
                    if session.get('session_id') == session_id:
                        return cls(**session)
        return None

    @classmethod
    def destroy_by_session_id(cls, session_id):
        """ Destroy a session by session_id """
        file_path = 'user_sessions.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                data = [session for session in data
                        if session.get('session_id') != session_id]
            with open(file_path, 'w') as f:
                json.dump(data, f)

    def to_dict(self):
        """ Convert the session instance to a dictionary """
        return {'user_id': self.user_id, 'session_id': self.session_id}
