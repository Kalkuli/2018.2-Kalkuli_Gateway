from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS

import requests

from project.api.data_extraction.specs.extract import extract_data

data_extraction_blueprint = Blueprint('data_extraction', __name__)
CORS(data_extraction_blueprint)

@data_extraction_blueprint.route('/api/v1/interpret_data', methods=['POST'])
@swag_from(extract_data)
def interpret():
    post_data = request.get_json()

    intepret_response = requests.post(
        'https://nvv696n4mc.execute-api.sa-east-1.amazonaws.com/dev/interpret',
        json=post_data
    )

    return jsonify({
        "receipt": intepret_response.json()
    })
