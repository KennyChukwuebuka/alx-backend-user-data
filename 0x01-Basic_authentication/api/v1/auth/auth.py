#!/usr/bin/env python3
""" Module of Auth
"""
# File: api/v1/auth/auth.py

from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        :param path: The path to check.
        :param excluded_paths: A list of paths
        :return: False for now. Logic to be implemented later.
        """
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request.
        :param request: The Flask request object.
        :return: None for now.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request.
        :param request: The Flask request object.
        :return: None for now.
        """
        return None