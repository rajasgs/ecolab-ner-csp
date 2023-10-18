'''



'''

from . import api
from flask import current_app as app
from flask import request

import random

# Local import
from .response_utils import JSON_MIME_TYPE, success_, success_json

'''
'''
@api.route('/template')
def template_index():   
    
    r_number = random.randint(0, 1000)

    result_json = {
        'result': r_number,
        
        'api_error': 0
    }
    
    return success_json(result_json)