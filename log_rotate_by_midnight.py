import logging
from logging import handlers

LOG_FILENAME = 'mylog.txt'

def log_rotate_by_midnight(path):
    logformatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')
    log = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, 'midnight', 1, backupCount=5)
    log.setLevel(logging.DEBUG)
    log.setFormatter(logformatter)

    tmp = logging.getLogger('main')
    tmp.addHandler(log)
    tmp.setLevel(logging.DEBUG)
    return tmp

logger = log_rotate_by_midnight(LOG_FILENAME)
logger.error('writting this message to log')
