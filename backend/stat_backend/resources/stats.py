from operator import and_
from flask_restful import Resource
from models.stats import StatisticsModel
from datetime import date
from sqlalchemy import extract, and_


class StatisticsList(Resource):
    def get(self, country, sort_field):
        today = date.today()
        if sort_field == "deaths":
            field = StatisticsModel.deaths
        else:
            field = StatisticsModel.date_value

        records = (StatisticsModel.query.filter(
            and_(
                StatisticsModel.country_code == country.upper(),
                extract("year", StatisticsModel.date_value) == today.year,
            )).order_by(field).all())
        return {"statistics": list(map(lambda r: r.json(), records))}, 200
