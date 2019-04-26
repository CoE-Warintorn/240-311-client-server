__version__ = '0.1'

from flask import Flask
from flask_cors import CORS

from . import settings
from . import views
from . import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.config.from_envvar('BOOK_SETTINGS')

    cors = CORS(app, resource={r'/api/*': {'origin': '*'}})

    models.init_db(app)
    views.register_blueprint(app)

    return app