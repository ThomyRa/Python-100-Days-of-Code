import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv

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


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("success.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
