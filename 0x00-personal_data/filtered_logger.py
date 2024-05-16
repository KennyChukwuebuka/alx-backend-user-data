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
import logging


def filter_datum(fields, redaction, message, separator):
    pattern = r'({0}=)([^{0}]+)'.format('|'.join(fields))
    return re.sub(pattern, r'\1' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record_dict = record.__dict__
        for field in self.fields:
            record_dict[field] = self.filter_datum(record_dict[field])
        return super().format(record)

    @staticmethod
    def filter_datum(data: str) -> str:
        return RedactingFormatter.REDACTION
