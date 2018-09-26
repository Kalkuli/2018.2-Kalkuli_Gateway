import os
from flask import Flask, jsonify
from flask_cors import CORS

from project.api.data_extraction.views import data_extraction_blueprint
from project.api.receipts.views import receipts_blueprint


def create_app(script_info=None):

    app = Flask(__name__)

    CORS(app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.register_blueprint(data_extraction_blueprint)
    app.register_blueprint(receipts_blueprint)

    return app
