import urllib.request
import json
import http.client
import datetime
from flask_restplus import Namespace, Resource, fields
import sqlalchemy
from stat_backend.models import StatisticsModel, UpdatesModel
from stat_backend.db import db
from flask import abort, Response


def request_api_data(start_date, end_date):
    request_url = f"https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{start_date:%Y-%m-%d}/{end_date:%Y-%m-%d}"

    response = urllib.request.urlopen(request_url)
    data = response.read()
    dict = json.loads(data)

    return dict


api_namespace = Namespace("api", descriptions="Available API operations")


def last_update_in_year(year):
    record = (UpdatesModel
              .query
              .filter(sqlalchemy.extract("year", UpdatesModel.date_value) == year)
              .oder_by("date_value")
              .last())
    return record[0]


@api_namespace.route("/update/")
class UpdateData(Resource):

    @api_namespace.doc("update_data")
    def get(self):
        """
        update records from COVID tracker
        """
        today = datetime.date.today()
        year = today.year
        start_date = datetime.date(year, 1, 1)
