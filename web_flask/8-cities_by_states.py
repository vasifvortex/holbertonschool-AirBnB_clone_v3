#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    """states"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
