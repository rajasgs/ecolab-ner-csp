'''



'''
import random
from flask import request, redirect

# Local import
# from .response_utils import JSON_MIME_TYPE, success_, success_json
from . import api
import colog
# import business.predict as pr

import business.bert_predict as bp

from custom_flask import render_template

LATEST_VERSION = 3

'''
    /
'''
@api.route('/bert')
def index_bert():   

    return render_template(
        'index_bert.html',
        version_number = LATEST_VERSION
    )

@api.route('/bert', methods=['POST'])
def result_bert():

    version_number = LATEST_VERSION

    print(f'version_number  : {version_number}')

    address = request.values.get('address').lower()
    
    result = bp.classify_address(address)

    # colog.info(result)

    # print(f'modelpath : {modelpath}')

    return render_template(
        'index_bert.html', 
        version_number  = version_number,
        address         = address,
        result          = result
    )




    