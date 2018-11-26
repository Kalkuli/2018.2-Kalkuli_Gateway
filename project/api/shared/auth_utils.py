from functools import wraps
import requests
import os

from flask import request, jsonify

def get_auth_status(request):
    auth_bearer = request.headers.get('Authorization')

    if not auth_bearer:
        response = {
            'is_logged': False,
            'error': {
                'content': {
                    'status': 'fail',
                    'message': 'Unauthorized'
                },
                'status_code': 401
            }
        }
        return response

    header = {'Authorization': auth_bearer}
    auth_response = requests.get(os.environ.get('USERS_PATH') + '/auth/status', headers=header)

    if auth_response.status_code != 200:
        response = {
            'is_logged': False,
            'error': {
                'content': auth_response.json(),
                'status_code': auth_response.status_code
            }
        }
        return response
    else:
        response = {
            'is_logged': True,
            'user': auth_response.json().get('data')
        }
        return response

def needs_authentication_with_company_id(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_status = get_auth_status(request)

        if not auth_status.get('is_logged'):
            return jsonify(auth_status.get('error').get('content')), auth_status.get('error').get('status_code')
        
        user = auth_status.get('user')

        user_company_id = user.get('company_id')
        request_company_id = kwargs.get('company_id')

        if user_company_id != int(request_company_id):
            error_message = {
                'status': 'fail',
                'message': 'Access Forbidden'
            }
            return jsonify(error_message), 403

        return f(*args, **kwargs)
    
    return decorated_function


def needs_authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_status = get_auth_status(request)

        if not auth_status.get('is_logged'):
            return jsonify(auth_status.get('error').get('content')), auth_status.get('error').get('status_code')

        return f(*args, **kwargs)

    return decorated_function
