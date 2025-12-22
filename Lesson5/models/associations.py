from extensions import db

gamers_game = db.Table(
        'gamer_game',
        db.Column('gamer_id', db.Integer, db.ForeignKey('gamer.id')),
        db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
    )