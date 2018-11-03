from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@users_blueprint.route('/api/v1/company', methods=['POST'])
def save_company():

    info = request.get_json()
    response = requests.post('http://172.20.0.1:5003/add_company', json=info)

    return jsonify(response.json()), response.status_code