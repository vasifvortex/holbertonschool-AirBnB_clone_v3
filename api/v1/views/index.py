#!/usr/bin/python3
"""Documentation"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def get_stats():
    json = {
        "amenities": storage.count(Amenity) if True else 0,
        "cities": storage.count(City) if True else 0,
        "places": storage.count(Place) if True else 0,
        "reviews": storage.count(Review) if True else 0,
        "states": storage.count(State) if True else 0,
        "users": storage.count(User) if True else 0
    }
    return jsonify(json)
