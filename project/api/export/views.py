from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests


exports_blueprint = Blueprint('exports', __name__)
CORS(exports_blueprint)


@exports_blueprint.route('/api/v1/export', methods=['POST'])
def export_csv():
    
    date = request.get_json()

    filter_receipts = requests.post('http://kalkuli-receipts.herokuapp.com/select_date',json=date)
    report = requests.post('http://kalkuli-reports.herokuapp.com/report', json=filter_receipts.json())

    response = requests.post('http://172.26.0.1:5007/export', json=report.json())
    
    return response.text, response.status_code
