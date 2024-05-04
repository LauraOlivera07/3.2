import logging, config

logging.basicConfig(level=logging.DEBUG,format=config.LOG_FORMAT,filename=config.LOG_PATH,filemode=config.LOG_MODE)

def debug(msg=''):
    logging.debug(msg)
def info(msg=''):
    logging.info(msg)

def error(msg='Error generico'):
    logging.error(msg)

def warning(msg='Warning generico'):
    logging.warning(msg)