#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
    Args:
        fields
        redaction
        messgage
        separator
"""


import re


def filter_datum(fields, redaction, message, separator):
    """filter_datum"""
    pattern = (
        r'(?:(?<=^)|(?<={0}))(?:{1}=)([^{1}{2}]+)'
        .format(separator, '|'.join(fields), separator)
    )
    return re.sub(pattern, redaction, message)
