from flask import Flask, jsonify, Blueprint, request
import requests

data_extraction_blueprint = Blueprint('data_extraction', __name__)


@data_extraction_blueprint.route('/api/v1/extract_data', methods=['POST'])
def extract_and_interpret():
    file = request.files['file']
    file.name = file.filename
    files = {'file': file}
    extract_response = requests.post(
        'http://172.21.0.1:5001/extract',
        files=files
    )

    intepret_response = requests.post(
        'http://172.25.0.1:5002/interpret',
        json=extract_response.json()
    )

    return jsonify({
        "receipt": intepret_response.json()
    })
