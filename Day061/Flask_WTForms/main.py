import os
from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import pdb

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


class LoginForm(FlaskForm):
    email = EmailField(label="email", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # pdb.set_trace()
    if login_form.validate_on_submit():
        print(f"The email is: {login_form.email.data}")
        if login_form.email.data == "admin@email.com" and login_form.password.data == "qwerty":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
