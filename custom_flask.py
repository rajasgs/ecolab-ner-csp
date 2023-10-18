
'''
Created on 

@author: Raja CSP Raman

source:
    ?
'''

from constants import *
import flask

def render_template(
    page_name,
    **kwargs
):

    return flask.render_template(
        page_name, 
        APP_TITLE = APP_TITLE,
        **kwargs
    )