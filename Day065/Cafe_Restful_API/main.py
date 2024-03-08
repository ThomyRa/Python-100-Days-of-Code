from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from prettyprinter import pprint
import random
import pdb


app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # Automatic Building the Response
    def to_dict(self):
        # Method 1
        # Looping through each column in the data record
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2
        # Dictionary comprehension for Method 1
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()

    # Manually Building the Response
    # return jsonify(
    #     cafe={
    #         # "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "amenities": {
    #             "has_sockets": random_cafe.has_sockets,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "seats": random_cafe.seats,
    #             "coffee_price": random_cafe.coffee_price,
    #         }
    #     })
    return random_cafe.to_dict()


@app.route("/all")
def get_all_cafes():
    results = db.session.execute(db.select(Cafe))
    all_cafes = results.scalars().all()
    all_cafes = [cafe.to_dict() for cafe in all_cafes]
    # pprint(all_cafes)
    return jsonify(
        cafes=all_cafes,
    )


@app.route("/search")
def find_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),

        )
    except KeyError:
        return jsonify(error={"Bad request": "Some or all fields were incorrect or missing"})
    else:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"Success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
