from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

from project.api.shared.auth_utils import needs_authentication


exports_blueprint = Blueprint('exports', __name__)
CORS(exports_blueprint)

@exports_blueprint.route('/api/v1/export', methods=['POST'])
@needs_authentication
def export_csv():
    
    date = request.get_json()

    response = requests.post(os.environ.get('EXPORT_PATH') + '/export', json=date)
    return response.text, response.status_code
