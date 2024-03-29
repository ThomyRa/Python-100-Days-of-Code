from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import smtplib
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name, email, phone, message)

        load_dotenv()
        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("PASSWORD")
        message = f"Subject:Greetings from Thomas' Blog\nDear {name} we are happy that you get in touch with us.\nBest Regards."
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)

        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html")


def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    return f"<h1> {name} | {email} | {phone} | {message} </h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
