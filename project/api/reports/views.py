from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests
import os

from project.api.shared.auth_utils import needs_authentication_with_company_id, needs_authentication

reports_blueprint = Blueprint('reports', __name__)
CORS(reports_blueprint)

@reports_blueprint.route('/api/v1/save_report', methods=['POST'])
@needs_authentication
def save_report():

    date = request.get_json()

    response = requests.post(os.environ.get('REPORTS_PATH') + '/add_report', json=date )

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/<company_id>/get_all_reports', methods=['GET'])
@needs_authentication_with_company_id
def get_all_reports(company_id):
    response = requests.get(os.environ.get('REPORTS_PATH') + f'/{company_id}/get_reports')
    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/<company_id>/report/<int:report_id>', methods=['DELETE'])
@needs_authentication_with_company_id
def delete_report(company_id, report_id):
    response = requests.delete(
        os.environ.get('REPORTS_PATH') + f'/{company_id}/report/{report_id}'
    )
    return jsonify(response.json()), response.status_code