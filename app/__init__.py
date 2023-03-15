from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config=Config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)
    db.init_app(app)

    return app

app = create_app()

with app.app_context():
    from .controllers import coleta
    db.create_all()
    app.register_blueprint(coleta.BLUEPRINT)