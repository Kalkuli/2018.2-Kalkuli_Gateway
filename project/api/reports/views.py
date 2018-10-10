from flask import Flask, jsonify, Blueprint, request
import requests

reports_blueprint = Blueprint('reports', __name__)


@reports_blueprint.route('/api/v1/report', methods=['POST'])
def generate_report():
    receipts = requests.get('http://kalkuli-receipts.herokuapp.com/receipts')
    response = requests.post('http://172.24.0.1:5004/report', json=receipts.json())
    return jsonify(response.json()), response.status_code
