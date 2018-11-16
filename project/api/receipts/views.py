from flask import Flask, jsonify, Blueprint, request
from flasgger import swag_from
from flask_cors import CORS
import requests
import os

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
        os.environ.get('RECEIPTS_PATH') + '/receipt',
        json=data
    )

    return jsonify(response.json()), response.status_code


@receipts_blueprint.route('/api/v1/<company_id>/receipts', methods=['GET'])
@swag_from(get_all)
@needs_authentication_with_company_id
def get_receipts(company_id):
    response = requests.get(os.environ.get('RECEIPTS_PATH') + f'/{company_id}/receipts')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/receipt/<int:receipt_id>', methods=['DELETE'])
@needs_authentication_with_company_id
def delete_receipt(company_id, receipt_id):
    response = requests.delete(
        os.environ.get('RECEIPTS_PATH') + f'/{company_id}/receipt/{receipt_id}'
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/tags', methods=['GET'])
@needs_authentication_with_company_id
def get_tags(company_id):
    response = requests.get(os.environ.get('RECEIPTS_PATH') + f'/{company_id}/tags')
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/update_tag/<int:receipt_id>', methods=['PATCH'])
@needs_authentication_with_company_id
def update_tag(company_id, receipt_id):
    data = request.get_json()
    response = requests.patch(
        os.environ.get('RECEIPTS_PATH') + f'/{company_id}/update_tag/{receipt_id}',
        json=data
    )
    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/create_tag', methods=['POST'])
@needs_authentication
def create_tag():
    data = request.get_json()

    response = requests.post(os.environ.get('RECEIPTS_PATH') + '/create_tag', json=data)

    return jsonify(response.json()), response.status_code

@receipts_blueprint.route('/api/v1/<company_id>/update_receipt/<int:receipt_id>', methods=['PUT'])
@needs_authentication_with_company_id
def update_receipt(company_id, receipt_id):
    data = request.get_json()
    response = requests.put(
        os.environ.get('RECEIPTS_PATH') + f'/{company_id}/update_receipt/{receipt_id}',
        json=data
    )
    return jsonify(response.json()), response.status_code