import os
from flask import Flask, render_template, session
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
    login_form.validate_on_submit()
    return render_template("success.html", form=login_form)


# @app.route("/logout.html")
# def logout():
#     session.clear()
#     return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
