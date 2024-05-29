#!/usr/bin/env python3
""" Auth module
"""

import hashlib


def _hash_password(password: str) -> bytes:
    """ Hash password
    Note: the returned bytes should be a salted hash of the input password
    hashed with bycrypt.hashpw
    """
    return hashlib.sha256(password.encode()).hexdigest().lower()
