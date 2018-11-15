from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests

from project.api.receipts.specs.add import add_specs
from project.api.receipts.specs.get import get_all

from project.api.shared.auth_utils import needs_authentication, needs_authentication_with_company_id

receipts_blueprint = Blueprint('receipts', __name__)
CORS(receipts_blueprint)

@receipts_blueprint.route('/api/v1/receipt', methods=['POST'])
@swag_from(add_specs)
@needs_authentication
def add_receipt():
    data = request.get_json()

    response = requests.post(
        'https://kalkuli-receipts-hom.herokuapp.com/receipt',
        json=data
    )

    return jsonify(response.json()), response.status_code


@receipts_blueprint.route('/api/v1/<company_id>/receipts', methods=['GET'])
@swag_from(get_all)
@needs_authentication_with_company_id
def get_receipts(company_id):
    response = requests.get(f'http://172.27.0.1:5006/{company_id}/receipts')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/receipt/<int:receipt_id>', methods=['DELETE'])
@needs_authentication_with_company_id
def delete_receipt(company_id, receipt_id):
    response = requests.delete(
        f'http://172.27.0.1:5006/{company_id}/receipt/{receipt_id}'
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/tags', methods=['GET'])
@needs_authentication_with_company_id
def get_tags(company_id):
    response = requests.get(f'http://172.27.0.1:5006/{company_id}/tags')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/update_tag/<int:receipt_id>', methods=['PATCH'])
@needs_authentication_with_company_id
def update_tag(company_id, receipt_id):
    data = request.get_json()
    response = requests.patch(
        f'http://172.27.0.1:5006/{company_id}/update_tag/{receipt_id}',
        json=data
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/create_tag', methods=['POST'])
@needs_authentication
def create_tag():
    data = request.get_json()

    response = requests.post('http://172.27.0.1:5006/create_tag', json=data)

    return jsonify(response.json()), response.status_code