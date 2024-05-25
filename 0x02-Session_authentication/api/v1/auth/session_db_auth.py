#!/usr/bin/env python3
""" Module of Session in Database
"""
# api/v1/auth/session_db_auth.py
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import uuid


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class to manage authentication
    using sessions stored in the database """

    def create_session(self, user_id=None):
        """ Create a session for a user_id """
        if user_id is None:
            return None

        session_id = str(uuid.uuid4())
        new_session = UserSession(user_id=user_id, session_id=session_id)
        new_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get user_id from session_id """
        if session_id is None:
            return None

        session = UserSession.find_by_session_id(session_id)
        if session:
            return session.user_id
        return None

    def destroy_session(self, request=None):
        """ Destroy the session based on the request cookie """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        UserSession.destroy_by_session_id(session_id)
        return True
