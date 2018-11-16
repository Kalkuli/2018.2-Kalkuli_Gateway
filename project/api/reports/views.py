from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests

from project.api.shared.auth_utils import needs_authentication_with_company_id, needs_authentication

reports_blueprint = Blueprint('reports', __name__)
CORS(reports_blueprint)


@reports_blueprint.route('/api/v1/report', methods=['POST'])
@needs_authentication
def generate_report():
    date = request.get_json()
    company_id = date.get('company_id')

    receipts = requests.post(f'https://kalkuli-receipts-hom.herokuapp.com/{company_id}/select_date', json=date)
    response = requests.post('https://kalkuli-reports-hom.herokuapp.com/report', json=receipts.json())

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/save_report', methods=['POST'])
@needs_authentication
def save_report():

    date = request.get_json()
    company_id = date.get('company_id')

    receipts = requests.post(f'https://kalkuli-receipts-hom.herokuapp.com/{company_id}/select_date', json=date)
    report_data = requests.post('https://kalkuli-reports-hom.herokuapp.com/report', json=receipts.json())

    period = date.get('period')
    date_to = period.get('date_to')
    date_from = period.get('date_from')

    data = {
        'company_id': company_id,
        'date_from': date_from,
        'date_to': date_to
    }
    response = requests.post('https://kalkuli-reports-hom.herokuapp.com/add_report', json=data)

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/<company_id>/get_all_reports', methods=['GET'])
@needs_authentication_with_company_id
def get_all_reports(company_id):
    response = requests.get(f'https://kalkuli-reports-hom.herokuapp.com/{company_id}/get_reports')
    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/<company_id>/report/<int:report_id>', methods=['DELETE'])
@needs_authentication_with_company_id
def delete_report(company_id, report_id):
    response = requests.delete(
        f'https://kalkuli-reports-hom.herokuapp.com/{company_id}/report/{report_id}'
    )
    return jsonify(response.json()), response.status_code