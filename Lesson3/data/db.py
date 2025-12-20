from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class BookModel(db.Model):

    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Author = db.Column(db.String(50), nullable=False)
    Year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.Title}"

with app.app_context():
    db.create_all()