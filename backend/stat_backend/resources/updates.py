from flask_restful import Resource
from models.updates import UpdatesModel
from models.stats import StatisticsModel
from datetime import date
from sqlalchemy import extract
from db import db
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

def get_country_list():
    return StatisticsModel.query.distinct(StatisticsModel.country_code).all()

class LastUpdate(Resource):
    def get(self):
        record = get_last_update()
        if record:
            return record.json()
        return {"message": "Updates not found in this year"}, 404

class CountryList(Resource):
    def get(self):
        countries = get_country_list()
        if countries:
            return countries
        return {"message": "There is no country lis"}, 404

class PerformUpdate(Resource):
    def get(self):
        today = date.today()
        start_date = date(today.year, 1, 1)
        last_update = get_last_update()
        if last_update:
            start_date = last_update.date_value
        
        stat_update = get_from_api(start_date, today)
        if stat_update["data"]:
            for record in stat_update["data"]:
                stat_rec = StatisticsModel(record["date_value"], record["country_code"])
                stat_rec.confirmed = record["confirmed"]
                stat_rec.deaths = record["death"]
                stat_rec.stringency = record["stringency"]
                stat_rec.stringency_actual = record["stringency_actual"]
                db.session.add(stat_rec)
            db.session.commit()

