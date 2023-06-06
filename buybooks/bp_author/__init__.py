from flask import Blueprint

bp_author = Blueprint('bp_author', __name__)

from . import views_author