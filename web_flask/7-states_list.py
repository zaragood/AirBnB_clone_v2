#!/usr/bin/python3
""" import Falsk"""
from flask import Flask, render_template
from models import storage
from models.state import State


"""script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
You must use the option strict_slashes=False in your route definition
"""
app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
    def states_list():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
