from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests

from project.api.receipts.specs.add import add_specs
from project.api.receipts.specs.get import get_all

receipts_blueprint = Blueprint('receipts', __name__)
CORS(receipts_blueprint)

@receipts_blueprint.route('/api/v1/receipt', methods=['POST'])
@swag_from(add_specs)
def add_receipt():
    data = request.get_json()

    response = requests.post(
        'https://kalkuli-receipts-hom.herokuapp.com/receipt',
        json=data
    )

    return jsonify(response.json()), response.status_code


@receipts_blueprint.route('/api/v1/receipts', methods=['GET'])
@swag_from(get_all)
def get_receipts():
    response = requests.get('https://kalkuli-receipts-hom.herokuapp.com/receipts')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/receipt/<int:receipt_id>', methods=['DELETE'])
def delete_receipt(receipt_id):
    response = requests.delete(
        'https://kalkuli-receipts-hom.herokuapp.com/receipt/%i' % receipt_id
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/tags', methods=['GET'])
def get_tags():
    response = requests.get('https://kalkuli-receipts-hom.herokuapp.com/tags')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/update_tag/<int:receipt_id>', methods=['PATCH'])
def update_tag(receipt_id):
    response = requests.patch(
        'https://kalkuli-receipts-hom.herokuapp.com/update_tag/%i' % receipt_id
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/create_tag', methods=['POST'])
def create_tag():
    data = request.get_json()

    response = requests.post('https://kalkuli-receipts-hom.herokuapp.com/create_tag', json=data)

    return jsonify(response.json()), response.status_code