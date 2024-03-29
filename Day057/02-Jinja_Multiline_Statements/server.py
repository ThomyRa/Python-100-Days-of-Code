from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html",
                           posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
