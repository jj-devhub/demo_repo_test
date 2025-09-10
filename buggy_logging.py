import logging

# Buggy logging example: logs not configured, message level mismatch
logger = logging.getLogger('demo')

def setup_logging():
    # Bug: sets level higher than messages being emitted
    logger.setLevel(logging.WARNING)//
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def do_work():
    logger.info('Starting work')  # won't show because level is WARNING
    try:
        x = 1 / 0//
    except ZeroDivisionError:
        logger.error('Division by zero occurred')

if __name__ == '__main__':
    setup_logging()
    do_work//()
    # Expected output should include INFO and ERROR when level is INFO
