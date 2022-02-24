import json
import urllib.request
from datetime import date, timedelta

from db import db
from flask_restful import Resource
from models.stats import StatisticsModel
from models.updates import UpdatesModel
from sqlalchemy import and_, extract

MAIN_URL = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/"


def get_last_update():
    today = date.today()
    record = (UpdatesModel.query.filter(
        extract("year", UpdatesModel.date_value) == today.year).order_by(
            UpdatesModel.date_value.desc()).first())
    return record


def get_from_api(start_date, end_date):
    request_url = MAIN_URL + f"{start_date:%Y-%m-%d}/{end_date:%Y-%m-%d}"
    print("request_url: ", request_url)

    response = urllib.request.urlopen(request_url)
    data = response.read()
    print("raw_data: ", data)
    dict = json.loads(data)

    return dict


def get_country_list():
    # return StatisticsModel.query.distinct(StatisticsModel.country_code).all()
    return StatisticsModel.query.with_entities(
        StatisticsModel.country_code).distinct()


def date_from_str(string_date):
    return (int(x) for x in string_date.split("-"))


class HealthCheck(Resource):
    def get(self):
        return "OK", 200


class LastUpdate(Resource):
    def get(self):
        record = get_last_update()
        if record:
            return record.json()
        return {"message": "Updates not found in this year"}, 204


class CountryList(Resource):
    def get(self):
        countries = get_country_list()
        if countries:
            return [c.country_code for c in countries]
        return {"message": "There is no country list"}, 204


class PerformUpdate(Resource):
    def get(self):
        today = date.today()
        start_date = date(today.year, 1, 1)
        last_update = get_last_update()
        if last_update:
            start_date = last_update.date_value + timedelta(days=1)
        if start_date > today:
            return {"message": "Already updated"}, 204

        try:
            stat_update = get_from_api(start_date, today)
        except Exception:
            return {
                "message": "Error in reffer to covidtrackerapi.bsg.ox.ac.uk"
            }, 404

        print("stat_update:", stat_update)
        print("stat_update type:", type(stat_update))
        if stat_update and stat_update["data"]:

            if UpdatesModel.query.filter(
                    and_(UpdatesModel.date_value == today,
                         UpdatesModel.records == 0)).first():
                return {"message": "Last update is not completed yet"}, 202

            update_record = UpdatesModel(today, 0)
            db.session.add(update_record)
            db.session.commit()
            db.session.refresh(update_record)
            # print(stat_update["data"])
            for key_date in stat_update["data"]:
                for country in stat_update["data"][key_date]:
                    record = stat_update["data"][key_date][country]
                    record_date = date(*date_from_str(record["date_value"]))
                    stat_rec = StatisticsModel(record_date,
                                               record["country_code"])
                    stat_rec.confirmed = record["confirmed"]
                    stat_rec.deaths = record["deaths"]
                    stat_rec.stringency = record["stringency"]
                    stat_rec.stringency_actual = record["stringency_actual"]
                    db.session.add(stat_rec)
            update_record.records = len(stat_update["data"])
            db.session.commit()
