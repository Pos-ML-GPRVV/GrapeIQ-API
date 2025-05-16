from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 
from service.web_scrapping.web_scrapping import WebScrapping
from datetime import datetime
from utils.env import validate_env_variables
from utils.api_doc_info import SWAGGER_TEMPLATE
app = Flask(__name__)

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
    "title": "GrapeIQ API",
    "uiversion": 3,
    "info": SWAGGER_TEMPLATE["info"]
}

swagger = Swagger(app, template=SWAGGER_TEMPLATE)

auth = HTTPBasicAuth()

def get_current_year():
    return str(datetime.now().year)

@app.route("/")
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
    """
    year = request.args.get("year", default=2023)
    data_web_scrapping = WebScrapping().get_content_page(year)
    return jsonify({"data": data_web_scrapping, "year": year})


@app.route("/json")
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
            description: Data successfully retrieved
            schema:
                type: object
                properties:
                    success:
                        type: boolean
                        description: Indicates if the request was successful
                    year:
                        type: integer
                        description: The year the data refers to
                    data:
                        type: array
                        description: List of grape commercialization records
                        items:
                            type: object
        500:
            description: Internal server error
            schema:
                $ref: '#/components/schemas/HTTPError'
    """
    try:
        year = request.args.get("year", type=int, default=2023)
        data_web_scrapping = WebScrapping().get_content_page_json(year)
        response = {
            "success": True,
            "year": year,
            "data": data_web_scrapping
        }
        return jsonify(response)
    except Exception as e:
        error_response = {
            "success": False,
            "year": year,
            "error": str(e)
        }
        return jsonify(error_response), 500


if __name__ == "__main__":
    validate_env_variables()
    app.run(debug=True, host='0.0.0.0', port=5432)
