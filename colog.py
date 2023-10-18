'''
Created on 

Course work: 

'''

import logging
import inspect
import os
import time
from dotenv import load_dotenv

load_dotenv()

LOG_FILE_NAME = os.getenv('LOG_FILE_NAME')

logging.basicConfig(
    filename    = LOG_FILE_NAME, 
    level       = logging.DEBUG,
    format      = '%(asctime)s %(levelname)s %(module)s : %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S'
)

# this will set the UTC time instead of local
logging.Formatter.converter = time.gmtime

def get_linenumber(current_frame):
    return current_frame.f_back.f_lineno

def get_class_name(content):

    if('/' not in content):
        return '_'

    content_parts   = content.split('/')
    last_part       = content_parts[len(content_parts) - 1]

    return last_part

def get_log_base(curframe, calframe):

    line_no  = get_linenumber(curframe)
    log_base = f'[{str(calframe[1].filename)}:{line_no}][{str(calframe[1][3])}]'

    return log_base

def combine_params(*args):

    string_part = ""
    for arg in args:
        string_part += str(arg) + " "

    return string_part

def info(*args):

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)

    current_log_base    = get_log_base(curframe, calframe)
    string_part         = combine_params(*args)
    class_part          = f'{current_log_base} {string_part}'

    logging.info(class_part)

def warning(*args):

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)

    current_log_base    = get_log_base(curframe, calframe)
    string_part         = combine_params(*args)
    class_part          = f'{current_log_base} {string_part}'

    logging.warning(class_part)

def error(*args):

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)

    current_log_base    = get_log_base(curframe, calframe)
    string_part         = combine_params(*args)
    class_part          = f'{current_log_base} {string_part}'

    logging.error(class_part)