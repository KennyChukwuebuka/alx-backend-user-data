#!/usr/bin/env python3
""" Auth module
"""

import hashlib
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash password
    Note: the returned bytes should be a salted hash of the input password
    hashed with bycrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
