from flask import Flask, render_template
from extensions import db, migrate
from datetime import date, datetime
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


with app.app_context():
    db.create_all()

@app.route('/fill_table')
def fill_table_data():
    dev1 = GameDeveloper(
        firstName="John",
        lastName="Carmack",
        country="USA",
        birthday=date(1970, 8, 20)
    )

    dev2 = GameDeveloper(
        firstName="Hideo",
        lastName="Kojima",
        country="Japan",
        birthday=date(1963, 8, 24)
    )

    db.session.add_all([dev1, dev2])
    db.session.flush()

    game1 = Game(
        name="Doom",
        genre="fps",
        releaseDate=datetime(1993, 12, 10),
        developer=dev1
    )

    game2 = Game(
        name="Metal Gear Solid",
        genre="adventure",
        releaseDate=datetime(1998, 9, 3),
        developer=dev2
    )

    db.session.add_all([game1, game2])
    db.session.flush()

    gamer1 = Gamer(startDate=date(2022, 1, 1))
    gamer2 = Gamer(startDate=date(2023, 6, 15))

    db.session.add_all([gamer1, gamer2])
    db.session.flush()

    profile1 = Profile(
        nickname="PlayerOne",
        gamer=gamer1
    )

    profile2 = Profile(
        nickname="Snake",
        gamer=gamer2
    )

    db.session.add_all([profile1, profile2])

    gamer1.games.append(game1)
    gamer1.games.append(game2)

    gamer2.games.append(game2)

    db.session.commit()

    return "Test data created"

@app.route('/')
def index():
    developers = GameDeveloper.query.all()
    gamers = Gamer.query.all()
    return render_template('index.html', developers=developers, gamers=gamers)

if __name__ == '__main__':
    app.run()