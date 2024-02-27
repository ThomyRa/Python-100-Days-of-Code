from flask import Flask, render_template, request, redirect, url_for
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from prettyprinter import pprint
import pdb


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


current_path = os.getcwd()
db_path = f"{current_path}/books_collection.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)


with app.app_context():
    db.create_all()

# all_books = []


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = results.scalars()
    # pdb.set_trace()

    return render_template('index.html', book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit-rating", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get("id")
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit-rating.html', book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
