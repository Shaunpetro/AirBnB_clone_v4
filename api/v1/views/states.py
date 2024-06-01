#!/usr/bin/python3
"""
Module for handling State objects and operations
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """
    Retrieves all State objects
    """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """
    Retrieves a specific State object by ID
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """
    Creates a new State object
    """
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, description="Not a JSON")
    if "name" not in state_json:
        abort(400, description="Missing name")

    new_state = State(**state_json)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """
    Updates a specific State object by ID
    """
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, description="Not a JSON")
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    for key, value in state_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200

@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a State object by ID
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
