#!/usr/bin/python3
"""
endpoint for states
"""
from flask import jsonify, request, abort

from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route("/states/<state_id>/cities", strict_slashes=False)
def cities(state_id: str):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    cities = [city.to_dict() for city in state.cities]

    return jsonify(cities), 200


@app_views.route("/cities/<city_id>", strict_slashes=False)
def city(city_id: str):
    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    return jsonify(city.to_dict()), 200


@app_views.route("/cities/<city_id>",
                 methods=["DELETE"],
                 strict_slashes=False)
def delete_city(city_id: str):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities",
                 methods=["POST"],
                 strict_slashes=False)
def add_city(state_id: str):
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    data = request.get_json()

    if data.get("name") is None:
        return jsonify({"error": "Missing name"}), 400

    data["state_id"] = state_id

    city = City(**data)

    city.save()

    return jsonify(city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"], strict_slashes=False)
def update_city(city_id: str):

    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400

    data: dict = request.get_json()

    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(city, key, value)

    city.save()

    return jsonify(city.to_dict()), 200