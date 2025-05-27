from flask import jsonify
from datetime import datetime
from utils.messages import MESSAGES

def get_timestamp():
    return datetime.utcnow().isoformat()

def build_json_response(
        message_key="SUCCESS",
        data=None,
        year=None, 
        status_code=200):
    
    msg = MESSAGES.get(message_key, MESSAGES["GENERIC_ERROR"])
    
    response = {
        "success": True,
        "code": msg["code"],
        "message": msg["message"],
        "timestamp": get_timestamp(),
        "data": {
            "year": year,
            "data": data if data is not None else []
        }
    }
    return jsonify(response), status_code

def build_error_response(message_key="GENERIC_ERROR", status_code=400):
    msg = MESSAGES.get(message_key, MESSAGES["GENERIC_ERROR"])

    response = {
        "success": False,
        "code": msg["code"],
        "message": msg["message"],
        "timestamp": get_timestamp()
    }
    return jsonify(response), status_code
