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

    company_id = date.get('company_id')

    filter_receipts = requests.post(os.environ.get('RECEIPTS_PATH') + f'/{company_id}/select_date',json=date)

    report = requests.post(os.environ.get('REPORTS_PATH') + '/report', json=filter_receipts.json())

    response = requests.post(os.environ.get('EXPORT_PATH') + '/export', json=report.json())
    
    return response.text, response.status_code
