from flask import Flask


def create_backend():
    app = Flask(__name__)
    from backend import storage
    app.register_blueprint(storage.bp)
    return app
