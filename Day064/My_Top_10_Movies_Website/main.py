import os
import sqlalchemy.exc
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
import requests
from dotenv import load_dotenv
from prettyprinter import pprint
import pdb


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)


class MovieForm(FlaskForm):
    title = StringField('Movie Name', validators=[DataRequired()])
    # year = StringField('Year', validators=[DataRequired()])
    # description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars()
    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    movies_info = {}
    url = 'https://api.themoviedb.org/3/search/movie'
    form = MovieForm()
    if form.validate_on_submit():
        params = {
            "query": request.form["title"],
            "include_adult": False,
        }
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv("MOVIES_TOKEN")}"
        }
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        movie_list = (response.json()["results"])
        # pprint(movie_list)
        return render_template("select.html", options=movie_list)

    return render_template("add.html", form=form)


@app.route("/select")
def get_movie_details():
    movie_id = request.args.get("movie_id")
    # print(movie_id)
    movie_details_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv("MOVIES_TOKEN")}"
    }
    response = requests.get(url=movie_details_url, headers=headers)
    response.raise_for_status()
    movie_details = response.json()
    # pprint(movie_details)
    img_backdrop_path = movie_details["backdrop_path"]
    movie_title = movie_details["title"]
    movie_release_year = movie_details["release_date"]
    movie_overview = movie_details["overview"]
    # print(img_backdrop_path, movie_title, movie_release_year, movie_overview)

    images_url = 'https://api.themoviedb.org/3/configuration'
    img_response = requests.get(url=images_url, headers=headers)
    img_response.raise_for_status()
    image_data = img_response.json()["images"]
    base_url = image_data["secure_base_url"]
    # print(base_url)

    new_movie = Movie(
        title=movie_title,
        year=movie_release_year.split("-")[0],
        description=movie_overview,
        rating=None,
        ranking=None,
        review=None,
        img_url=f"{base_url}/original{img_backdrop_path}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
