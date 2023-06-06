from flask import Blueprint

bp_book = Blueprint('bp_book', __name__)


from . import views_book