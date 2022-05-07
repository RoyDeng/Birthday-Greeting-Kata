import logging
import logging.config
import os
from colorlog import ColoredFormatter
from logging.handlers import TimedRotatingFileHandler

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(base_dir, "logs/api", "api.log")


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


LOG_LEVEL = os.getenv('LOG_LEVEL')
if LOG_LEVEL == 'DEBUG':
    log_level = logging.DEBUG
elif LOG_LEVEL == 'INFO':
    log_level = logging.INFO
else:
    log_level = logging.DEBUG


@singleton
class Logger:
    """Basic logging configuration."""
    def __init__(self):
        """init."""
        sh_formatter = ColoredFormatter(
            '%(log_color)s%(levelname)-5s%(reset)s '
            '%(bold_yellow)s[%(asctime)s]%(reset)s%(white)s '
            '%(name)s %(funcName)s %(yellow)s%(module)s/ %(bold_purple)s:%(lineno)d%(reset)s '
            '%(log_color)s%(message)s%(reset)s',
            datefmt='%y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'bold_blue',
                'INFO': 'bold_cyan',
                'WARNING': 'bold_red,',
                'ERROR': 'bg_bold_red',
                'CRITICAL': 'red,bg_white',
            }
        )

        tr_formatter = ColoredFormatter(
            '%(levelname)s '
            '[%(asctime)s] '
            '%(name)s %(funcName)s%(module)s/ : '
            '%(message)s ---end---%(reset)s',
            datefmt='%y-%m-%d %H:%M:%S',
        )

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # StreamHandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(sh_formatter)

        # Store log
        tr = TimedRotatingFileHandler(LOG_PATH, when="midnight", interval=1,backupCount=5)
        tr.setLevel(logging.INFO)
        tr.setFormatter(tr_formatter)

        # Add handlers
        logger.addHandler(tr)
        logger.addHandler(sh)

        self.logger = logger

    def __getattr__(self, name):  # noqa
        return getattr(self.logger, name)


logger = Logger().logger
