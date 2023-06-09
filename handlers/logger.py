import os
import sys
import logging
import datetime

from settings import LOG_LEVEL, LOG_FORMAT, LOG_DIR


class LoggArch(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        level = LOG_LEVEL

        self.setLevel(level)

        log_format = logging.Formatter(LOG_FORMAT)

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(log_format)

        self.addHandler(console_handler)

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        file_handler = logging.FileHandler(
            os.path.join(LOG_DIR, f'{current_date}.log'),
            encoding='utf-8'
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(log_format)

        self.addHandler(file_handler)

        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)