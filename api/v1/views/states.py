#!/usr/bin/python3
"""Documentation"""
from flask import abort, jsonify, request, Response
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False)
def states():
    states = storage.all(State)
    return jsonify([state.to_dict() for state in states.values()])


@app_views.route("/states/<state_id>", strict_slashes=False)
def state(state_id):
    states = storage.all(State)
    state = states[f"State.{state_id}"]
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", strict_slashes=False, methods=["DELETE"])
def del_state(state_id):
    states = storage.all(State)
    state = states.get(state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({})


@app_views.route("/states", strict_slashes=False, methods=["POST"])
def post_state():
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    
    state = State()
    if request.get_json("name"):
        state.name = request.get_json("name")
        state.save()
    else:
        return jsonify({"error": "Missing name"}), 400

    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", strict_slashes=False, methods=["PUT"])
def put_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    
    data = request.get_json()
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value) 
    
    state.save()

    return jsonify(state.to_dict()), 200
    