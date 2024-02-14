from flask import Flask
from flask import render_template
import random
import datetime as dt
import requests
import pdb

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_date = dt.datetime.now()
    current_year = current_date.year
    return render_template("index.html",
                           num=random_number,
                           year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = "https://api.genderize.io"
    age_url = "https://api.agify.io"
    parameters = {
        "name": name,
    }

    gender_response = requests.get(url=gender_url, params=parameters)
    gender_response.raise_for_status()
    # pdb.set_trace()
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_response = requests.get(url=age_url, params=parameters)
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",
                           name=str(name).capitalize(),
                           gender=gender,
                           age=age)


if __name__ == "__main__":
    app.run(debug=True)


