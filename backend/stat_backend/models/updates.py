from db import db


class UpdatesModel(db.Model):
    __tablename__ = "updates"

    id = db.Column(db.Integer, primary_key=True)
    date_value = db.Column(db.Date, nullable=False, index=True)
    records = db.Column(db.Integer, default=0)

    def __init__(self, date_value, records):
        self.date_value = date_value
        self.records = records

    def json(self):
        return {
            "date_value": f"{self.date_value:%Y-%m-%d}",
            "records": self.records
        }

    @classmethod
    def find_by_date(cls, search_date):
        return cls.query.filter_by(date_value=search_date).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
