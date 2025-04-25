from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 
from flask_caching import Cache 
from service.web_scrapping.web_scrapping import WebScrapping

app = Flask(__name__)

app.config["SWAGGER"] = {"title": "Web Scrapping API", "uiversion": 3}

swagger = Swagger(app)

auth = HTTPBasicAuth()

cache = Cache(app, config={"CACHE_TYPE": "simple"}) #configurando cache da aplicação


@app.route("/")
@cache.cached(timeout=10) #guarda em cache durante 10 segundos
def store():
    data_web_scrapping = WebScrapping().get_content_page()
    return str(data_web_scrapping)


if __name__ == "__main__":
    app.run(debug=True)
