from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"  # Лучше использовать os.urandom(24) в реальных проектах
    app.register_blueprint(bp)
    return app
