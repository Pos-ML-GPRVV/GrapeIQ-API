import os
from flask import Flask, jsonify, request
from flask import Flask, jsonify, request, send_file
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 
from app.service.web_scrapping.web_scrapping import WebScrapping
from datetime import datetime
from app.utils.env import validate_env_variables
from app.utils.api_doc_info import SWAGGER_TEMPLATE
from functools import wraps
from app.utils.dict_to_csv import dict_to_csv, zip_files
from pathlib import Path
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='static')

app.config["SWAGGER"] = {
    "specs": [{
        "endpoint": "apispec",
        "route": "/apispec.json",
        "rule_filter": lambda rule: True,
        "model_filter": lambda tag: True,
    }],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "Grapi",
    "uiversion": 3,
    "info": SWAGGER_TEMPLATE["info"]
}

API_KEY = os.getenv("API_KEY")

swagger = Swagger(app, template=SWAGGER_TEMPLATE)

auth = HTTPBasicAuth()

CORS(app, resources={r"/*": {"origins": ["https://tech-challange-front.onrender.com", "http://localhost:3000"]}})

def get_current_year():
    return str(datetime.now().year)

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key == API_KEY:
            return func(*args, **kwargs)
        else:
            return jsonify({"message": "Unauthorized"}), 401
    return wrapper

@app.route("/extractor")
@cross_origin()
@require_api_key
def get_raw_data():
    """
    Returns raw data obtained through web scraping
    ---
    tags:
      - Data Collection
    summary: Get Raw Grape Data
    description: Retrieves raw data about grape commercialization for a specific year
    parameters:
      - name: year
        in: query
        type: string
        required: false
        default: current year
        description: Target year for data collection
    responses:
        200:
            description: Data successfully retrieved
            schema:
                type: object
                properties:
                    code:
                        type: number
                        description: Status code of the operation
                    data:
                        type: object
                        properties:
                            data:
                                type: object
                                description: Raw data from web scraping
                            year:
                                type: string
                                description: Year of the data
                    message:
                        type: string
                        description: Operation status message
                    success:
                        type: boolean
                        description: Indicates if the operation was successful
                    timestamp:
                        type: string
                        format: date-time
                        description: Timestamp of the operation
        401:
            description: Unauthorized access
            schema:
                type: object
                properties:
                    message:
                        type: string
                        description: Unauthorized message
    """
    year = request.args.get("year", default=2023)
    if int(year) > 2023:
        return jsonify({"error": "Data available until 2023"}), 400 
    data_web_scrapping = WebScrapping().get_content_page(year)
    response = {
        "code": 200,
        "message": "Operation completed successfully",
        "success": True,
        "timestamp": datetime.now().isoformat(),
        "data": {
            "year": str(year),
            "data": data_web_scrapping,
        }
    }
    return jsonify(response)


@app.route("/download")
@cross_origin()
@require_api_key
def get_structured_data():
    """
    Returns processed data in a structured JSON format
    ---
    tags:
      - Data Collection
    summary: Get Structured Grape Data
    description: Retrieves processed and structured data about grape commercialization for a specific year
    parameters:
      - name: year
        in: query
        type: integer
        required: false
        default: current year
        description: Target year for data collection
    responses:
        200:
            description: Data successfully downloaded
        500:
            description: Internal server error
            schema:
                $ref: '#/components/schemas/HTTPError'
    """

    year = request.args.get("year", default=2023)
    if int(year) > 2023:
        return jsonify({"error": "Data available until 2023"}), 400 

    data_web_scrapping = WebScrapping().get_content_page(year)
    path_files = dict_to_csv(data_web_scrapping)
    zip_path = zip_files(path_files, year)
    path_resolve = Path(zip_path).resolve()
    return send_file(path_resolve, as_attachment=True)

if __name__ == "__main__":
    validate_env_variables()
    app.run(debug=True, host='0.0.0.0', port=5432)
