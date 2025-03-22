from flask import Blueprint

bp = Blueprint('main', __name__)

from my_app.main import routes
