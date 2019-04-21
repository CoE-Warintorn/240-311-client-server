from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    app.config.from_envvar('BOOK_SETTINGS')

    cors = CORS(app, resource={r'/api/*': {'origin': '*'}})

    return app