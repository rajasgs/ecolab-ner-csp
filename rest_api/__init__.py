from flask import Blueprint

api = Blueprint('rest_api', __name__)

from .template_controller import *
from .ml_controller import *
from .bert_controller import *