from extensions import db


class CarModel(db.Model):

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Year = db.Column(db.Integer, nullable=False)

    CarBrandId = db.Column(
        db.Integer,
        db.ForeignKey('car_brand.Id'),
        nullable=False
    )

    def __repr__(self):
        return f"<CarModel: {self.Name}({self.Year}) - {self.Price}$ >"