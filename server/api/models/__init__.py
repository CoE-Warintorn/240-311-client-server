from flask_mongoengine import MongoEngine
from .books import Book

db = MongoEngine()

def init_db(app):
    db.init_app(app)