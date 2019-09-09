import logging

#create the logger object
logger = logging.getLogger("camera_module")

#set the logger level
logger.setLevel(logging.DEBUG)
#logging.INFO, logging.DEBUG, logging.PRODUCTION

#create the file handler to record the logs
log_file = logging.FileHandler("patni.log")

#set the formatter to the file handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_file.setFormatter(formatter)

#attach logger with the log file
logger.addHandler(log_file)


logger.info('this is a log message')
logger.debug('this is a debug log message')
