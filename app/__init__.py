from flask import Flask
from .config import configobj

#
# app = create_app()


def create_app(mode='development'):
    app = Flask(__name__)
    register_blueprint(app)
    app.config.from_object(configobj[mode])
    register_plugin(app)
    return app


def register_plugin(app):
    from models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprint(app):
    from api.v1 import create_blueprint_v1
    blueprint = create_blueprint_v1()
    app.register_blueprint(blueprint, url_prefix='/v1')
