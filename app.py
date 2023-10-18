'''
    Multiple controllers:
        
        
'''

from flask import Flask
from rest_api import *
import os

import business.predict as pr

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8071))

    pr.initiate()
    
    app.run(
        host            = host, 
        port            = port, 
        debug           = True,
        use_reloader    = False
    )