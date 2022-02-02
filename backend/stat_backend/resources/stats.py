from operator import and_
from flask_restful import Resource, reqparse
from models.stats import StatisticsModel
from datetime import date
from sqlalchemy import extract, and_


class StatisticsList(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country")
        parser.add_argument("sort_field")
        args = parser.parse_args()
        today = date.today()
        country = args["country"]
        sort_field = args["sort_field"]
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
