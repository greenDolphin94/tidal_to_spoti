import os
import datetime

from .config import LOG_DIR, LOG_INFO_FILE, LOG_ERR_FILE

def logInfo(s, mode='a'):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    with open(LOG_INFO_FILE, mode, encoding='utf-8') as oFile:
        oFile.write(f"{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S.%f')} INFO {s}\n")

def logErr(s, mode='a'):
    with open(LOG_INFO_FILE, mode, encoding='utf-8') as oFile:
        oFile.write(f"{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S.%f')} ERR {s}\n")
    with open(LOG_ERR_FILE, mode, encoding='utf-8') as oFile:
        oFile.write(f"{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S.%f')} ERR {s}\n")