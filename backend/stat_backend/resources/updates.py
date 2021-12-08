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

def date_from_str(string_date):
    return (int(x) for x in string_date.split("-"))

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
            update_record = UpdatesModel(today, 0)
            db.session.add(update_record)
            db.session.commit()
            db.session.refresh(update_record)
            # print(stat_update["data"])
            for key_date in stat_update["data"]:
                for country in stat_update["data"][key_date]: 
                    record = stat_update["data"][key_date][country]
                    record_date = date(*date_from_str(record["date_value"]))
                    stat_rec = StatisticsModel(record_date, record["country_code"])
                    stat_rec.confirmed = record["confirmed"]
                    stat_rec.deaths = record["deaths"]
                    stat_rec.stringency = record["stringency"]
                    stat_rec.stringency_actual = record["stringency_actual"]
                    db.session.add(stat_rec)
            update_record.records = len(stat_update["data"])
            db.session.commit()

