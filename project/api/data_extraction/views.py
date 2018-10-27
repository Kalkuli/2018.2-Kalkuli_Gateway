from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS

import requests

from project.api.data_extraction.specs.extract import extract_data

data_extraction_blueprint = Blueprint('data_extraction', __name__)
CORS(data_extraction_blueprint)

@data_extraction_blueprint.route('/api/v1/extract_data', methods=['POST'])
@swag_from(extract_data)
def extract_and_interpret():
    file = request.files['file']
    file.name = file.filename
    files = {'file': file}
    extract_response = requests.post(
        'http://172.21.0.1:5001/extract',
        files=files
    )

    intepret_response = requests.post(
        'https://nvv696n4mc.execute-api.sa-east-1.amazonaws.com/dev/interpret',
        json=extract_response.json()
    )

    return jsonify({
        "receipt": intepret_response.json()
    })
