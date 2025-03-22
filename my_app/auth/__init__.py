from flask import Blueprint

bp = Blueprint('auth', __name__)


from my_app.auth import routes
