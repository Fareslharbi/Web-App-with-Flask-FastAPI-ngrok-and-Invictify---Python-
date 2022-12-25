import os
import datetime

BASE_DIR = os.path.dirname(__file__)
logger_dir = os.path.join(BASE_DIR, 'logs')
os.makedirs(logger_dir, exist_ok=True)

def trigger_log_save():
    filename = f"{datetime.datetime.now()}.txt"
    filepath = os.path.join(logger_dir, filename)
    with open(filepath, 'w+') as f:
        f.write('')