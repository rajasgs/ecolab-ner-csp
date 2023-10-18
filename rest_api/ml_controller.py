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
    /ml/base
'''
@api.route('/ml/base')
def api_base():   
    
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


# def get_request_values(request):

#     rargs = request.args 

#     marks                       = rargs.get('marks', type = int)
#     projects                    = rargs.get('projects', type = int)
#     articles                    = rargs.get('articles', type = int)
#     network                     = rargs.get('network', type = int)
#     relatives                   = rargs.get('relatives', type = int)
#     trendy_topic_knowledge      = rargs.get('trendy_topic_knowledge', type = int)
#     research_work               = rargs.get('research_work', type = int)
#     personality_mirroring       = rargs.get('personality_mirroring', type = int)
#     luck                        = rargs.get('luck', type = int)
#     demand_and_supply_factor    = rargs.get('demand_and_supply_factor', type = int)

#     return \
#         marks, projects, articles, network, relatives, \
#         trendy_topic_knowledge, research_work, personality_mirroring, \
#         luck, demand_and_supply_factor

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