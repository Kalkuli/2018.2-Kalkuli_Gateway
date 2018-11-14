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


@receipts_blueprint.route('/api/v1/<company_id>/receipts', methods=['GET'])
@swag_from(get_all)
def get_receipts(company_id):
    auth_bearer = request.headers.get('Authorization')

    if not auth_bearer:
        error_message = {
            'status': 'fail',
            'message': 'Unauthorized'
        }
        return jsonify(error_message), 401

    header = {'Authorization': auth_bearer}
    auth_response = requests.get('https://kalkuli-users-hom.herokuapp.com/auth/status', headers=header)
    user_company_id = None

    if auth_response.status_code == 200:
        content = auth_response.json()
        user_company_id = content.get('data').get('company_id')
    else:
        return jsonify(auth_response.json()), auth_response.status_code

    if user_company_id == int(company_id):
        response = requests.get(f'http://172.27.0.1:5006/{company_id}/receipts')
        return jsonify(response.json()), response.status_code
    else:
        error_message = {
            'status': 'fail',
            'message': 'Access Forbidden'
        }
        return jsonify(error_message), 403



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