from flask import Flask
from . import books

def register_blueprint(app):
    app.register_blueprint(books.module)