from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os


exports_blueprint = Blueprint('exports', __name__)
CORS(exports_blueprint)


@exports_blueprint.route('/api/v1/export', methods=['POST'])
def export_csv():
    
    date = request.get_json()

    filter_receipts = requests.post(os.environ.get('RECEIPTS_PATH') + '/select_date',json=date)
    report = requests.post(os.environ.get('REPORTS_PATH') + '/report', json=filter_receipts.json())

    response = requests.post(os.environ.get('EXPORT_PATH') + '/export', json=report.json())
    
    return response.text, response.status_code
