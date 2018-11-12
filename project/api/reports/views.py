from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
import requests

reports_blueprint = Blueprint('reports', __name__)
CORS(reports_blueprint)


@reports_blueprint.route('/api/v1/report', methods=['POST'])
def generate_report():

    date = request.get_json()

    receipts = requests.post('https://kalkuli-receipts-hom.herokuapp.com/select_date',json=date)
    response = requests.post('https://kalkuli-reports-hom.herokuapp.com/report', json=receipts.json())

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/save_report', methods=['POST'])
def save_report():

    date = request.get_json()
    receipts = requests.post('https://kalkuli-receipts-hom.herokuapp.com/select_date', json= date)
    report_data = requests.post('https://kalkuli-reports-hom.herokuapp.com/report', json=receipts.json())

    period = date.get('period')
    date_to = period.get('date_to')
    date_from = period.get('date_from')

    data = {
        'date_from': date_from,
        'date_to': date_to
    }
    response = requests.post('https://kalkuli-reports-hom.herokuapp.com/add_report', json=data)

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/get_all_reports', methods=['GET'])
def get_all_reports():
    response = requests.get('https://kalkuli-reports-hom.herokuapp.com/get_reports')
    return jsonify(response.json()), response.status_code