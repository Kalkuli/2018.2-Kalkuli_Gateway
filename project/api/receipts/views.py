from flask import Flask, jsonify, Blueprint, request
import requests

receipts_blueprint = Blueprint('receipts', __name__)


@receipts_blueprint.route('/api/v1/receipt', methods=['POST'])
def add_receipt():
    data = request.get_json()

    response = requests.post(
        'http://172.27.0.1:5006/receipt',
        json=data
    )

    return jsonify(response.json()), response.status_code
