import os

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from resources.stats import StatisticsList
from resources.updates import LastUpdate, CountryList, PerformUpdate


def create_app():
    application = Flask(__name__)
    api = Api(application, prefix="/api")

    api.add_resource(StatisticsList, "/stats/<string:country>/<string:sort_field>")
    api.add_resource(PerformUpdate, "/update")
    api.add_resource(LastUpdate, "/last_update")
    api.add_resource(CountryList, "/countries")

    from db import db, db_config
    application.config.update(db_config)
    db.init_app(application)
    migrate = Migrate(application, db)
    application.db = db


    return application

if __name__=="__main__":
    app = create_app()
    app.run(port=5000, debug=True)
