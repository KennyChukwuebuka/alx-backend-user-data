#!/usr/bin/env python3
"""
    Filtered Logger
"""

import re
import logging


def filter_datum(fields: list, redaction: str, message:
                 str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


if __name__ == '__main__':
    log = logging.getLogger('test_logger')
    log.setLevel(logging.INFO)
    log.info('Test log')
