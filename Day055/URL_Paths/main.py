from flask import Flask

app = Flask(__name__)


def make_bold(f):
    def wrapper():
        return f'<b>{f()}</b>'
    return wrapper


def make_emphasis(f):
    def wrapper():
        return f'<em>{f()}</em>'
    return wrapper


def make_underline(f):
    def wrapper():
        return f'<u>{f()}</u>'
    return wrapper


@app.route("/")
def hello_world():
    return ('<h1 style="text-align:center">Hello World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODBqejU2ZDBvcDQ4Z2tqMjRtaTl0eGliZml3N3A2dzdsenFxZ3U5cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif" width=200px>')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"


# To run the Flask app from IDE in debug mode
if __name__ == "__main__":
    app.run(debug=True)
