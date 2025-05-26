from flask import jsonify
from datetime import datetime

def get_timestamp():
    return datetime.utcnow().isoformat()

def build_json_response(
        data=None,
        year=None,
        message=None,
        success=True,
        status_code=200):

    if message is None:
        message = "Operation completed successfully" if success else "Operation failed"

    response = {
        "success": success,
        "message": message,
        "timestamp": get_timestamp(),
        "data": {
            "year": year,
            "data": data if data is not None else []
        }
    }
    return jsonify(response), status_code


def build_error_response(
        message=None,
        status_code=400):
    
    if message is None:
        message = "An error occurred during execution"

    response = {
        "success": False,
        "message": message,
        "timestamp": get_timestamp()
    }
    return jsonify(response), status_code