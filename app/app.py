from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 
from flask_caching import Cache 


app = Flask(__name__)

app.config["SWAGGER"] = {"title": "Web Scrapping API", "uiversion": 3}

swagger = Swagger(app)

auth = HTTPBasicAuth()

cache = Cache(app, config={"CACHE_TYPE": "simple"}) #configurando cache da aplicação


@app.route("/")
@cache.cached(timeout=60) #guarda em cache durante 10 segundos
def store():
    from service.web_scrapping.web_scrapping import WebScrapping
    ano = request.args.get("ano", default="2019")  # Ano padrão
    data_web_scrapping = WebScrapping().get_content_page()
    return str(data_web_scrapping)


@app.route("/json")
@cache.cached(timeout=60)
def store_json():

    from service.web_scrapping.web_scrapping import WebScrapping
    ano = request.args.get("ano", type=int, default="1970")  # Ano padrão

    data_web_scrapping = WebScrapping().get_content_page_json(ano)
    return str(data_web_scrapping)


if __name__ == "__main__":
    app.run(debug=True)
