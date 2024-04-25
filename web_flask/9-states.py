#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def list_cities_by_states():
    """states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.values())


@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """states"""
    states = storage.all(State)
    states_val = states.values()
    for state in states_val:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return """<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
