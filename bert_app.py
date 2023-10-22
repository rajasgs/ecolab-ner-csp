'''
    Multiple controllers:
        
        
'''

from flask import Flask
from rest_api import *
import os
import sys

from simpletransformers.ner import NERModel
import business.bert_predict as bp

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8071))

    user_port       = sys.argv[1]

    port = int(os.environ.get('PORT', user_port))

    bp.model = NERModel('bert', 'outputs/', use_cuda=False)

    # bp.set_dict('house three')
    
    app.run(
        host            = host, 
        port            = port, 
        debug           = True,
        use_reloader    = False
    )