#!/usr/bin/env python3
"""
    Filtered Logger
"""

import re
import logging


def filter_datum(fields: list[str], redaction: str, message:
                 str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Returns a logger object"""
    return logging.getLogger('user_data')


def main() -> None:
    """Main function"""
    logger = get_logger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.info(filter_datum(['name', 'email', 'phone'],
                             'XXX', 'Bob loblaw', ';'))


if __name__ == "__main__":
    main()
