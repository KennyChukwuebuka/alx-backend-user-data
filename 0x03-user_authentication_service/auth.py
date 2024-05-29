#!/usr/bin/env python3
""" Auth module
"""

import hashlib


def _hash_password(password: str) -> bytes:
    """ Hash password
    """
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        b'',
        100000
    )
