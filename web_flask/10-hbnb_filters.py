#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """states"""
    states = storage.all(State)
    states_val = states.values()
    amenities = storage.all(Amenity)
    amenities_val = amenities.values()
    print(amenities_val)
    return render_template("10-hbnb_filters.html", states=states_val, amenities=amenities_val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
