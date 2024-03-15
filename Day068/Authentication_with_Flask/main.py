import os

import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Creates a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            password=request.form.get("password"),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get("email"),
            password=hash_and_salted_password,
            name=request.form.get("name"),
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to DB
        login_user(new_user)
        # Redirects and get name from the current_user
        return render_template("secrets.html", name=request.form.get("name"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # Checks stored password hash against entered password hashdd
        if check_password_hash(user.passeord, password):
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(
        "static",
        path="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
