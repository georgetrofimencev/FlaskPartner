import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

config = {
    "development": "config.modes.DevelopmentConfig",
    "testing": "config.modes.TestingConfig",
    "default": "config.modes.DevelopmentConfig",
    "production": "config.modes.ProductionConfig",
}


def create_app(config_mode: str = None):
    app = Flask(__name__, instance_relative_config=True, )
    config_name = config_mode if config_mode \
        else os.getenv('FLASK_CONFIGURATION', 'default')

    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    return app
