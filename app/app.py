from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 
from service.web_scrapping.web_scrapping import WebScrapping
from datetime import datetime
from utils.env import validate_env_variables
from utils.api_doc_info import SWAGGER_TEMPLATE
from utils.response_builder import build_json_response, build_error_response, MESSAGES


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
    "title": "Grapi",
    "uiversion": 3,
    "info": SWAGGER_TEMPLATE["info"]
}

swagger = Swagger(app, template=SWAGGER_TEMPLATE)

auth = HTTPBasicAuth()

def get_current_year():
    current_year = datetime.now().year
    return build_json_response("SUCCESS", data=[current_year])


@app.route("/extractor")
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
    if int(year) > 2023:
        return build_error_response("DATA_LIMIT_YEAR") 
    data_web_scrapping = WebScrapping().get_content_page(year)
    return build_json_response("SUCCESS", year=year, data=data_web_scrapping)


@app.route("/download")
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
    pass #TODO Criar rota de download


if __name__ == "__main__":
    validate_env_variables()
    app.run(debug=True)
