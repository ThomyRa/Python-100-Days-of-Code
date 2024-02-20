from flask import Flask
from flask import render_template
import requests
import pdb
from prettyprinter import pprint

api_url = "https://api.npoint.io/f514f220d9477e85f50a"

response = requests.get(url=api_url)
response.raise_for_status()
posts_data = response.json()
pprint(posts_data)
# pdb.set_trace()


app = Flask(__name__)


@app.route("/")
def home():
    # pdb.set_trace()
    return render_template("index.html", all_posts=posts_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
