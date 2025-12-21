from flask import Flask, render_template
from extensions import db, migrate
from models import CarModel, CarBrand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

@app.route('/fill_database')
def fill_database():

    car_brand = CarBrand.query.filter_by(Name="Mercedes").first()
    if not car_brand:
        car_brand = CarBrand(Name="Mercedes", OriginCountry="Germany")
        db.session.add(car_brand)

    car_models = CarModel.query.all()
    if not car_models:
        car_model = CarModel(Name="EQS SUV", Year=2018, Price=150550.0, CarBrandId=car_brand.Id)
        db.session.add(car_model)

        car_model = CarModel(Name="GLA", Year=2020, Price=45450.0, CarBrandId=car_brand.Id)
        db.session.add(car_model)

        car_model = CarModel(Name="Classe G", Year=2021, Price=176151.0, CarBrandId=car_brand.Id)
        db.session.add(car_model)

    db.session.commit()

    return "Database filled successfully"


@app.route('/')
def brands_list():

    brands = CarBrand.query.all()
    return render_template('index.html', brands=brands)


if __name__ == '__main__':
    app.run()