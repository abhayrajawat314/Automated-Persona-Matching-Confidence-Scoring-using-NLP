import logging
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime
import os
from src.constants import ROOT_PATH


# define constants 
LOG_DIR='logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

log_dir_path=os.path.join(ROOT_PATH,LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path=os.path.join(log_dir_path,LOG_FILE)

def configure_logger():

    #creating logger
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    #creating handlers
    consoleHandler=logging.StreamHandler()
    fileHandler=RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_SIZE,backupCount=BACKUP_COUNT)
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    #setting formatter
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.DEBUG)

    #addig handlers
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

#configure the logger
configure_logger()





