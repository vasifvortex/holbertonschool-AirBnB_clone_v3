#!/usr/bin/python3
'''Doc for users'''
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    '''Doc for users'''
    users = storage.all("User")
    return jsonify([user.to_dict() for user in users.values()])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''Doc for users'''
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''Doc for users'''
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    '''Doc for users'''
    user = request.get_json(silent=True)
    if user is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "email" not in user.keys():
        return jsonify({"error": "Missing email"}), 400
    if "password" not in user.keys():
        return jsonify({"error": "Missing password"}), 400
    new_user = User(**user)
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    '''Doc for users'''
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    update = request.get_json(silent=True)
    if update is None:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in update.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
