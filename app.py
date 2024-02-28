'''
    Multiple controllers:
        
        
'''

from flask import Flask
from rest_api import *
import os
import sys

# import business.predict as pr
import business.validator_single as vas

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8071))

    # model_version   = sys.argv[1]
    user_port       = sys.argv[1]

    port = int(os.environ.get('PORT', user_port))

    pr.initiate()

    # print(f'model_version : {model_version}')

    vas_singlton = vas.ValidatorSingleton.getInstance(model_version = None)
    
    app.run(
        host            = host, 
        port            = port, 
        debug           = True,
        use_reloader    = False
    )


'''
How to run?
    py app.py <port_no>

    py app.py 9090
'''