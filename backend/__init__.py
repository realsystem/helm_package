from flask import Flask
from backend import api


def create_backend():
    app = Flask(__name__)
    app.register_blueprint(api.bp)
    return app
