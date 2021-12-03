from stat_backend.db import db


class StatisticsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_value = db.Column(db.Date, nullable=False, index=True)
    country_code = db.Column(db.String(3), nullable=False, index=True)
    confirmed = db.Column(db.Integer, default=0)
    deaths = db.Column(db.Integer, default=0)
    stringency_actual = db.Column(db.Numeric(10,2), default=0.00)
    strigency = db.Column(db.Numeric(Numeric(10,2), default=0.00)


class UpdatesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_value = db.Column(db.Date, nullable=False, index=True)
    records = db.Column(db.Integer, default=0)
