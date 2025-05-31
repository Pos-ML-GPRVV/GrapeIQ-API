SWAGGER_TEMPLATE = {
    "info": {
        "title": "Grapi",
        "description": """
![Grapi Logo](/static/Grapi-logo.png)

# About the API
API developed to collect and provide data about grape and grape products commercialization in Brazil.
The data is obtained through web scraping from [Embrapa's VitiBrasil portal](http://vitibrasil.cnpuv.embrapa.br/index.php).

## Team
- **⁠Gustavo Imbelloni**
  - [GitHub](https://github.com/gustavoimbelloni)
  - [LinkedIn](https://www.linkedin.com/in/gustavoimbelloni/)

- **⁠Patrick Meirelles**
  - [GitHub](https://github.com/PatrickMeirelles)
  - [LinkedIn](https://www.linkedin.com/in/patrick-meirelles/)

- **Raíssa Campos dos Santos**
  - [GitHub](https://github.com/raissacsantos)
  - [LinkedIn](https://www.linkedin.com/in/ra%C3%ADssa-campos-dos-santos-51780625a/)

- **Vitor Nogueira Domingos**
  - [GitHub](https://github.com/vitornogueirad)
  - [LinkedIn](https://www.linkedin.com/in/vitor-nogueira-domingos/)
  
- **Vitor Crispim**
  - [GitHub](https://github.com/vtCrispim)
  - [LinkedIn](https://www.linkedin.com/in/vitor-crispim-7b3481179/)

## Features
- Automated data collection
- Performance caching
- Interactive documentation
- Standardized JSON format

## Repositories
For more information, visit our repositories: 
- [API Repository](https://github.com/Pos-ML-GPRVV/Grapi)
- [Website Repository](https://github.com/Pos-ML-GPRVV/Grapi-Website)
"""
    },
    "components": {
        "schemas": {
            "HTTPError": {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "error": {"type": "string"}
                }
            }
        }
    }
}