import logging
import os
from datetime import datetime

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Define log directory path
logs_path = os.path.join(os.getcwd(), "logs")
# Create logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging_config = {
    'filename': LOG_FILE_PATH,
    'format': '%(name)s | %(asctime)s | line: %(lineno)d | Level: %(levelname)s | Message: %(message)s',
    'level': logging.INFO
}

logging.basicConfig(**logging_config)

if __name__ == "__main__":
    logging.info("Logging has started")
