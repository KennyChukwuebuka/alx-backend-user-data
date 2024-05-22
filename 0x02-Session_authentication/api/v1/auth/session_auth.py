#!/usr/bin/env python3
"""
Module of Session Authentication
"""

from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """ Session Authentication Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return self.user_object_from_id(user_id)
