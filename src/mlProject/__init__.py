import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Inside the logs folder it will save all the logs.
        logging.StreamHandler(sys.stdout)  # On the terminal it will print all the logs.
    ]
)

logger = logging.getLogger("mlProjectLogger") # Initializing the logger...