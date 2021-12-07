from flask_restful import Resource
from models.updates import UpdatesModel
from models.stats import StatisticsModel
from datetime import date
from sqlalchemy import extract
import urllib.request, json


def get_last_update():
    today = date.today()
    record = (
            UpdatesModel.query.filter(
                extract("year", UpdatesModel.date_value) == today.year
            )
            .order_by(UpdatesModel.date_value.desc())
            .first()
        )
    return record

def get_from_api(start_date, end_date):
    request_url = f"https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{start_date:%Y-%m-%d}/{end_date:%Y-%m-%d}"

    response = urllib.request.urlopen(request_url)
    data = response.read()
    dict = json.loads(data)

    return dict

class LastUpdate(Resource):
    def get(self):
        record = get_last_update()
        if record:
            return record.json()
        return {"message": "Updates not found in this year"}, 404


class PerformUpdate(Resource):
    def get(self):
        pass
