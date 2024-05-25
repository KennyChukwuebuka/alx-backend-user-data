#!/usr/bin/env python3
""" Module of Session in Database
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id=None):
        # Create a new UserSession instance and store it in the database
        session = UserSession(user_id=user_id)
        session.save()
        # Return the session ID
        return session.session_id

    def user_id_for_session_id(self, session_id=None):
        # Retrieve the UserSession from the database based on the session ID
        session = UserSession.get_session_by_id(session_id)
        if session:
            return session.user_id
        else:
            return None

    def destroy_session(self, request=None):
        # Get the session ID from the request cookie
        session_id = request.cookies.get('session_id')
        # Delete the UserSession from the database based on the session ID
        UserSession.delete_session(session_id)
