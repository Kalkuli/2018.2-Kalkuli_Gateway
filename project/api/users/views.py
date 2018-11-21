from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests
import os

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@users_blueprint.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()

    response = requests.post(
        os.environ.get('USERS_PATH') + '/auth/register',
        json=data
    )
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    data = request.get_json()

    response = requests.post(
        os.environ.get('USERS_PATH') + '/auth/login',
        json=data
    )
    return jsonify(response.json()), response.status_code

@users_blueprint.route('/api/v1/auth/logout', methods=['GET'])
def logout_user():
    auth_bearer = requests.headers.get('Authorization')
    error_response = {
        'message': 'Invalid payload',
        'status': 'fail'
    }

    if not auth_bearer:
        return jsonify(error_response), 401

    header = {'Authorization': auth_bearer}
    response = requests.get(
        os.environ.get('USERS_PATH') + '/auth/logout',
        headers=header
    )
    return jsonify(response.json()), response.status_code