from flask import Blueprint
from views.v1 import unified_prefix

api = Blueprint('source', __name__, url_prefix=f'{unified_prefix}')
from views.v1.source.view import *