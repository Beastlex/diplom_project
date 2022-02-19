from stat_backend.db import db


class StatisticsModel(db.Model):
    __tablename__ = "statistics"

    id = db.Column(db.Integer, primary_key=True)
    date_value = db.Column(db.Date, nullable=False, index=True)
    country_code = db.Column(db.String(3), nullable=False, index=True)
    confirmed = db.Column(db.Integer, default=0)
    deaths = db.Column(db.Integer, default=0)
    stringency_actual = db.Column(db.Numeric(10, 2), default=0.00)
    stringency = db.Column(db.Numeric(10, 2), default=0.00)

    def __init__(self, date_value, county_code):
        self.date_value = date_value
        self.country_code = county_code

    def json(self):
        return {
            "date_value": f"{self.date_value:%Y-%m-%d}",
            "country_code": self.country_code,
            "confirmed": self.confirmed,
            "deaths": self.deaths,
            "stringency_actual": f"{self.stringency_actual:.2f}",
            "stringency": f"{self.stringency:.2f}",
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
