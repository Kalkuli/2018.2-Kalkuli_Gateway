from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@users_blueprint.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()

    response = requests.post(
        'https://kalkuli-users-hom.herokuapp.com/auth/register',
        json=data
    )
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    data = request.get_json()

    response = requests.post(
        'https://kalkuli-users-hom.herokuapp.com/auth/login',
        json=data
    )
    return jsonify(response.json()), response.status_code
