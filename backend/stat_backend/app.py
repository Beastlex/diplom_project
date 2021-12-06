import os

from flask import Flask
from flask_migrate import Migrate
from flask_restplus import Api

from models import StatisticsModel, UpdatesModel


def create_app():
    from stat_backend.api_namespace import api_namespace

    application = Flask(__name__)
    api = Api(application, version="0.1", title="Statistics COVID-19 Backend API",
              description="Simple API for wrapper for 3d service")

    from stat_backend.db import db, db_config
    application.config["RESTPLUS_MASK_SWAGGER"] = False
    application.config.update(db_config)
    db.init_app(application)
    migrate = Migrate(application, db)
    application.db = db

    application.add_namespace(api_namespace)

    return application
