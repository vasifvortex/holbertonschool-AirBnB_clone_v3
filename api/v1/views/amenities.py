#!/usr/bin/python3
"""Amenities view module"""
from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Get amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return {"error": "Not found"}, 404
    return jsonify(amenity.to_dict())


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def get_all_amenity():
    """Get amenity by id"""
    amenities = storage.all("Amenity")
    return jsonify([amenity.to_dict() for amenity in amenities.values()])


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return {"error": "Not found"}, 404
    storage.delete(amenity)
    storage.save()
    return {}, 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def post_amenity():
    """Post a new amenity"""
    data = request.get_json(silent=True)
    if data is None:
        return {"error": "Not a JSON"}, 400
    if 'name' not in data:
        return {"error": "Missing name"}, 400
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity(amenity_id):
    """Put an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return {"error": "Not found"}, 404
    data = request.get_json(silent=True)
    if data is None:
        return {"error": "Not a JSON"}, 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
