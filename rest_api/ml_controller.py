'''



'''
import random
from flask import request

# Local import
from .response_utils import JSON_MIME_TYPE, success_, success_json
from . import api
import colog
import business.predict as pr

from custom_flask import render_template

'''
    /
'''
@api.route('/')
def index():   
    
    result = pr.predict()

    colog.info(result)

    result_json = {
        'result': int(result),
        
        'api_error': 0
    }
    
    # return success_json(result_json)

    return render_template(
        'index.html'
    )

@api.route('/', methods=['POST'])
def result():

    address = request.values.get('address')
    
    result = address

    print(f'result : {result}')

    return render_template(
        'index.html', 
        result = result
    )



'''
    /ml/base
'''
@api.route('/ml/regular')
def api_regular():  

    address = request.values.get('address')
    
    result = pr.predict()

    colog.info(result)

    result_json = {
        'result': int(result),
        
        'api_error': 0
    }
    
    # return success_json(result_json)

    return render_template(
        'index.html'
    )


'''
    /ml/base
'''
@api.route('/ml/<version_number>/predict')
def api_dynamic_versions(version_number):   

    print(f'version_number  : {version_number}')

    result = pr.predict()

    colog.info(result)

    result_json = {
        'result': int(result),
        
        'api_error': 0
    }
    
    return success_json(result_json)