from extensions import db


class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    releaseDate = db.Column(db.DateTime, nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    gameDeveloperId = db.Column(
        db.Integer,
        db.ForeignKey('developer.id'),
        nullable=False,
    )

    @property
    def Description(self):
        return f"{self.name} ({self.releaseDate.year}) - {self.genre}"