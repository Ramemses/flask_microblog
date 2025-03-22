from flask import Blueprint

bp = Blueprint('errors', __name__)

from my_app.errors import handlers
