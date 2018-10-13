from flask import Flask, jsonify, Blueprint, request
import requests

reports_blueprint = Blueprint('reports', __name__)


@reports_blueprint.route('/api/v1/report', methods=['POST'])
def generate_report():

    date = request.get_json()

    receipts = requests.get('http://172.21.0.1:5006/select_date',json=date.json())
    response = requests.post('http://172.22.0.1:5004/report', json=receipts.json())

    return jsonify(response.json()), response.status_code

@reports_blueprint.route('/api/v1/save_report', methods=['POST'])
def save_report():

    date = request.get_json()

    receipts = requests.get('http://172.21.0.1:5006/select_date', json= date.json())
    report = requests.post('http://172.22.0.1:5004/report', json=receipts.json())
    response = requests.post('http://172.22.0.1:5004/add_report', json=report.json())

    return jsonify(response.json()), response.status_code

