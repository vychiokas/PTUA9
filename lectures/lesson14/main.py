import logging
import logging.config

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger("sampleLogger")

logger.debug('This is a debug message')
logger.critical('This is a debug message')


print("1234")