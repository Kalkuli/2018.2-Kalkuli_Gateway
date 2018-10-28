import os
from flask import Flask, jsonify
from flasgger import Swagger

from project.api.data_extraction.views import data_extraction_blueprint
from project.api.receipts.views import receipts_blueprint
from project.api.reports.views import reports_blueprint
from project.api.export.views import exports_blueprint


def create_app(script_info=None):

    app = Flask(__name__)

    swag = Swagger(app, config={
        'headers': [],
        'specs': [
            {
                'endpoint': 'apispec',
                'route': '/apispec.json'
            }
        ],
        'openapi': '3.0.1',
        "swagger_ui": True,
        "static_url_path": "/flasgger_static",
        "specs_route": "/apidocs/"
    })

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.register_blueprint(data_extraction_blueprint)
    app.register_blueprint(receipts_blueprint)
    app.register_blueprint(reports_blueprint)
    app.register_blueprint(exports_blueprint)

    return app
