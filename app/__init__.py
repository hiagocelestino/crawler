from flask import Flask
from app.config import Config

def create_app(config=Config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    return app

app = create_app()

with app.app_context():
    from .controllers import *