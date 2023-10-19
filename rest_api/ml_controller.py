'''



'''
import random
from flask import request, redirect

# Local import
from .response_utils import JSON_MIME_TYPE, success_, success_json
from . import api
import colog
import business.predict as pr

from custom_flask import render_template

# LATEST_VERSION = 2

'''
    /
'''
@api.route('/')
def index():   

    # return render_template(
    #     'index.html',
    #     version_number = LATEST_VERSION
    # )

    return redirect(f"/v1")

# @api.route('/', methods=['POST'])
# def result():

#     print(f'version_number  : {version_number}')

#     address = request.values.get('address').lower()
    
#     result, modelpath = pr.classify_address(
#         address, 
#         model_version = version_number
#     )

#     # colog.info(result)

#     print(f'modelpath : {modelpath}')

#     return render_template(
#         'index_with_version.html', 
#         version_number  = version_number,
#         address         = address,
#         result          = result, 
#         modelpath       = modelpath
#     )



'''
    /
'''
@api.route('/<version_number>')
def index_with_version(version_number):   

    return render_template(
        'index_with_version.html',
        version_number = version_number,
    )


'''
    /ml/base
'''
@api.route('/<version_number>', methods=['POST'])
def api_dynamic_versions(version_number):   

    print(f'version_number  : {version_number}')

    address = request.values.get('address').lower()
    
    result, modelpath = pr.classify_address(
        address, 
        model_version = version_number
    )

    # colog.info(result)

    print(f'modelpath : {modelpath}')

    return render_template(
        'index_with_version.html', 
        version_number  = version_number,
        address         = address,
        result          = result, 
        modelpath       = modelpath
    )
    