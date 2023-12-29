#!/usr/bin/python3
""" import Falsk"""
from flask import Flask

"""script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
You must use the option strict_slashes=False in your route definition
"""
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display():
    return "Hello HBNB!"


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
