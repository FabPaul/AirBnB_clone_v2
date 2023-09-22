#!/usr/bin/python3
""" A script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return f'C ' + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    return f'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer """
    return f'{n} is a number'


if __name__ == "__main__":
    app.run('0.0.0.0')
