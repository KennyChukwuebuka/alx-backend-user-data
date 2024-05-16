#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
    Args:
        fields:
        redaction:
        message:
        separator:

"""

import re


import re

def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    return re.sub(rf'({"|".join(fields)})=.*?{separator}', rf'\1={redaction}{separator}', message)
