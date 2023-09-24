#!/usr/bin/python3
""" A script that starts a Flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2:
        num = "odd"
    else:
        num = "even"

    return render_template("6-number_odd_or_even.html", n=n, num=num)


@app.route("/state_list", strict_slashes=False)
def state_list():
    """display a HTML page for the states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page of the States and citites by state"""
    states = storage.all(State)
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('8-cities_by_states.html',
                           states=states, state_cities=cities)


@app.teardown_appcontext
def teardown(exception):
    """ Remove sqlalchemy session and close the db at the end of the req"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0')
