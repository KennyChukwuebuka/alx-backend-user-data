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


def get_logger() -> logging.Logger:
    """Returns a logger object"""
    return logging.getLogger('user_data')


def main() -> None:
    """Main function"""
    fields = ["password", "date_of_birth"]
    redaction = "XXX"
    message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
    separator = ";"
    print(
        filter_datum(fields, redaction, message, separator)
    )


if __name__ == "__main__":
    main()
