from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1"


@app.route("/bye")
def say_bye():
    return "<h1>Bye</h1>"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!!"


# To run the Flask app from IDE
if __name__ == "__main__":
    app.run(debug=True)
