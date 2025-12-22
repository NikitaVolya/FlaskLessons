from extensions import db


class GameDeveloper(db.Model):
    __tablename__ = 'developer'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(100), nullable=False)

    games = db.relationship('Game', backref='developer', lazy=True)