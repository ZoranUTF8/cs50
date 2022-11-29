from app import db


class Registrant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport_name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)

