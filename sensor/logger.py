import logging
import os
from datetime import datetime


#log file name

LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"

# log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

# create folder if not avaliable
os.makedirs(LOG_FILE_DIR,exist_ok=True)

# log file path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
format="[% (acstime)s ] %(lineno)d %(name)s - %(levelname) - %(message)s", 
level=logging.INFO,)