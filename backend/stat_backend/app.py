import os

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

# from models import StatisticsModel, UpdatesModel


def create_app():
    application = Flask(__name__)

    from db import db, db_config
    application.config.update(db_config)
    db.init_app(application)
    migrate = Migrate(application, db)
    application.db = db


    return application

if __name__=="__main__":
    app = create_app()
    app.run(port=5000, debug=True)
