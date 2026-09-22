# every exception that happens we should be able to log all that information in
# some files so that we will be able to track if there is any error even the custom exception
# error we will try to log that in the text file
import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d - %(name)s - %(message)s',
    level=logging.INFO,
)