import os
import json
from flask import Blueprint, jsonify, request

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/health", methods=["GET"])
def health_check():
    """
    Route: /health [GET]
    Health check endpoint to verify if the service is running.
    Returns a JSON response with status 200 if the service is up.
    """
    print(jsonify({ "status": 200, "message": "Service is running"}), 200)
    return jsonify({ "status": 200, "message": "Service is running"}), 200