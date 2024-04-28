#!/usr/bin/python3
"""Amenities view module"""
from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_all_places_for_city(city_id):
    """get all places for a city"""
    city = storage.get(City, city_id)
    if city is None:
        return {"error": "Not found"}, 404
    return jsonify([place.to_dict() for place in city.places])


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """get place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        return {"error": "Not found"}, 404
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """delete place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        return {"error": "Not found"}, 404
    storage.delete(place)
    storage.save()
    return {}, 200


@app_views.route('/cities/<city_id>/places', methods=["POST"],
                 strict_slashes=False)
def post_place(city_id):
    city = storage.get(City, city_id)
    if city is None:
        return {"error": "Not found"}, 404
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "user_id" not in data:
        return jsonify({"error": "Missing user_id"}), 400
    user = storage.get(User, data["user_id"])
    if user is None:
        return {"error": "Not found"}, 404
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    data['city_id'] = city_id
    new_place = Place(**data)
    storage.new(new_place)
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        return {"error": "Not found"}, 404
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
