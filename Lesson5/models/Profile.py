from extensions import db


class Profile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)

    gamerId = db.Column(db.Integer, db.ForeignKey('gamer.id'), nullable=False)
