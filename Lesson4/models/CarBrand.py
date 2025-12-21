from extensions import db


class CarBrand(db.Model):

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    OriginCountry = db.Column(db.String(80), nullable=False)

    Cars = db.relationship('CarModel', backref='car_brand', lazy=True)