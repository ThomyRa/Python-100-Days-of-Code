import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dotenv import load_dotenv


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)
ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('Post Name', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    authors_name = StringField("Author's Name", validators=[DataRequired()])
    img_url = StringField("Background Image", validators=[DataRequired(), URL()])
    body = StringField("Post Body", validators=[DataRequired()])
    submit = SubmitField('Submit')


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    today = date.today()
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title,
            subtitle=form.subtitle,
            author=form.authors_name,
            img_url=form.img_url,
            body=form.body,
            date=today.strftime('%B %d, %Y')
        )
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
