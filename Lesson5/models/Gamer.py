from extensions import db
from models.associations import gamers_game


class Gamer(db.Model):
    __tablename__ = 'gamer'

    id = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.Date, nullable=False)

    games = db.relationship('Game', secondary=gamers_game)

    profile = db.relationship('Profile', backref='gamer', uselist=False)