# Grapi - Grape Data Extraction API 

This API provides endpoints for extracting and processing grape commercialization data from http://vitibrasil.cnpuv.embrapa.br/index.php, using web scraping to collect up-to-date information.

![Logo](https://raw.githubusercontent.com/Pos-ML-GPRVV/Grapi/ca645c5663cbee149e6b27059cf53cb0550746d3/app/static/Grapi-logo.png) 

## 🚀 Features

- Raw data extraction about grape commercialization
- Data processing and structuring
- Download data in compressed CSV format
- Interactive documentation with Swagger
- API Key authentication
- CORS support for frontend integration

## 🛠️ Technologies Used

- Python 3.x
- Flask
- BeautifulSoup4
- Pandas
- Flask-HTTPAuth
- Flasgger (Swagger)
- Flask-CORS
- Gunicorn

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Environment variables configured (see Configuration section)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Pos-ML-GPRVV/Grapi
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```env
DB_HOST=db_host_here
DB_NAME=db_name_here
DB_USER=db_user_here
DB_PASSWORD=db_password_here
API_KEY=your_api_key_here
```

## 🚀 Running the Project

To run the project in development mode:

```bash
gunicorn app.app:app
```

The server will be available at `http://localhost:8000`

## 📚 API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/apidocs/`

## 🔑 Endpoints

### GET /extractor
Returns raw data obtained through web scraping.

**Parameters:**
- `year` (optional): Year for data collection (default: current year)

**Required Headers:**
- `x-api-key`: Your API key

### GET /download
Returns processed data in compressed CSV format.

**Parameters:**
- `year` (optional): Year for data collection (default: current year)

**Required Headers:**
- `x-api-key`: Your API key

## 🔒 Security

- API Key authentication
- CORS configured for specific origins
- Environment variables validation

## 🤝 Contributing

1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is under the [MIT](LICENSE) license.

## ✒️ Authors

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

## 📄 Notes

- Data is available until 2023
- API supports requests from specific origins (localhost:3000 and tech-challange-front.onrender.com) 
