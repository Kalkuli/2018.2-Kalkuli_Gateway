from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests

users_blueprint = Blueprint('users', __name__)
CORS(users_blueprint)

@reports_blueprint.route('/api/v1/company', methods=['POST'])
def save_company():

    info = request.get_json()

    response = requests.post('http://kalkuli-users.herokuapp.com/add_company', json=info)

    return jsonify(response.json()), response.status_code