#!/usr/bin/env python3
""" SessionDBAuth module for handling session with database persistence """

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import uuid
from datetime import datetime, timedelta
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class to manage user
    sessions with database persistence """

    def create_session(self, user_id=None):
        """ Creates a session ID and stores it in the database """
        if user_id is None:
            return None

        session_id = str(uuid.uuid4())
        session_duration = int(getenv('SESSION_DURATION', 0))
        expiration_time = (datetime.now() + timedelta(
            seconds=session_duration)).isoformat()

        new_session = UserSession(
            user_id=user_id, session_id=session_id,
            expiration_time=expiration_time)
        new_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns the user ID by session ID """
        if session_id is None:
            return None

        user_session = UserSession.find_by_session_id(session_id)
        if user_session is None:
            return None

        # Check if the session is expired
        if self.is_session_expired(user_session):
            UserSession.destroy_by_session_id(session_id)
            return None

        return user_session.user_id

    def is_session_expired(self, user_session):
        """ Check if the session is expired """
        if user_session.expiration_time is None:
            return False

        expiration_time = datetime.fromisoformat(user_session.expiration_time)
        return datetime.now() > expiration_time

    def destroy_session(self, request=None):
        """ Destroys the user session based on session ID
        from the request cookie """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        UserSession.destroy_by_session_id(session_id)
        return True
