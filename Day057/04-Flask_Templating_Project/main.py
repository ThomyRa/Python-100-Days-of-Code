from flask import Flask
from flask import render_template
import requests
from post import Post

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/blog/<post_id>")
def blog_entry(post_id):
    post = Post(posts[int(post_id) - 1])
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
