SWAGGER_TEMPLATE = {
    "info": {
        "title": "GrapeIQ API",
        "description": """
# About the API
API developed to collect and provide data about grape and grape products commercialization in Brazil.
The data is obtained through web scraping from Embrapa's VitiBrasil portal.

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

## Repository
For more information, visit our [GitHub Repository](https://github.com/Pos-ML-GPRVV/GrapeIQ-API)
""",
        "version": "1.0.0",
        "contact": {
            "email": "your.email@example.com",
            "url": "https://github.com/your-org/grapeiq-api"
        }
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