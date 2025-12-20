from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from data.db import *

@app.route("/books")
def books_list():
    books = []
    with app.app_context():
        books = BookModel.query.all()

    return render_template("books/index.html", books=books)

@app.route("/books/add")
def books_add_form():
    return render_template("books/add.html")

@app.route("/books/add", methods=["POST"])
def books_add():

    with app.app_context():
        new_book = BookModel(
            Title=request.form["title"],
            Author=request.form["author"],
            Year=int(request.form["year"]),
        )
        db.session.add(new_book)
        db.session.commit()
    return redirect("/books")

@app.route("/books/<int:book_id>/edit")
def books_edit_form(book_id: int):
    book = None

    with app.app_context():
        book = BookModel.query.get(book_id)

    return render_template("books/edit.html", book=book)

@app.route("/books/<int:book_id>/update", methods=["POST"])
def books_update(book_id: int):

    with app.app_context():
        book = BookModel.query.get(book_id)
        book.Title = request.form["title"]
        book.Author = request.form["author"]
        book.Year = int(request.form["year"])
        db.session.commit()

    return redirect("/books")

@app.route("/books/<int:book_id>/delete", methods=["POST"])
def books_delete(book_id: int):
    with app.app_context():
        book = BookModel.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
    return redirect("/books")