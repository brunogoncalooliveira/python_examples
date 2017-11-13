import logging
from logging import handlers

def log_rotate_by_midnight(path, namespace):
    logformatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')
    log = logging.handlers.TimedRotatingFileHandler(path, 'midnight', 1, backupCount=5)
    log.setLevel(logging.DEBUG)
    log.setFormatter(logformatter)

    tmp = logging.getLogger(namespace)
    tmp.addHandler(log)
    tmp.setLevel(logging.DEBUG)
    return tmp

logger1 = log_rotate_by_midnight('invalidapps.log', 'invalidapps_namespace')
logger2 = log_rotate_by_midnight('other.log', 'otherinvalidsomething_namespace')
