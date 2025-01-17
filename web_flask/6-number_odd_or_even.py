#!/usr/bin/python3
""" import Falsk"""
from flask import Flask
from markupsafe import escape
from flask import render_template

"""script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
You must use the option strict_slashes=False in your route definition
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/<text>", strict_slashes=False)
def python(text='cool'):
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
