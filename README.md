
# Grapi - Grape Commercialization Data Extraction API

This RESTful API, built with Python and Flask, extracts, processes, and makes available grape commercialization data in Brazil. It uses automated web scraping from the **Embrapa** website and stores the data in a **PostgreSQL** database hosted on **Neon**.

![Logo](https://raw.githubusercontent.com/Pos-ML-GPRVV/Grapi/master/app/static/Grapi-github.png)

---

## 🚀 Features

- Automated web scraping from Embrapa's grape commercialization site
- Structured and processed data available via REST API
- Interactive API documentation with Swagger (Flasgger)
- API Key authentication (using Flask-HTTPAuth)
- Data caching for performance optimization
- Data persistence in PostgreSQL (Neon)
- CORS support for frontend integration
- Download of processed data in compressed CSV format

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- BeautifulSoup4
- Pandas
- Requests
- PostgreSQL (Neon)
- Flask-HTTPAuth
- Flasgger (Swagger)
- Flask-CORS
- Gunicorn

---

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Neon account (managed PostgreSQL in the cloud)

---

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Pos-ML-GPRVV/Grapi
cd Grapi
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.env\Scriptsctivate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:

Create a `.env` file in the project root or copy from `.env.example`:
```env
DB_HOST='your-neon-db-host'
DB_NAME='your-db-name'
DB_USER='your-db-user'
DB_PASSWORD='your-db-password'
API_KEY='your_api_key'
```

> Use the credentials provided by Neon to connect to the database.

---

## 🚀 Running the Project

Run the app using Gunicorn in development mode:
```bash
gunicorn app.app:app
```

Or with Flask directly (optional):
```bash
python app/app.py
```

The API will be available at:  
`http://localhost:8000` (Gunicorn)  
or  
`http://localhost:5432` (Flask)

---

## 📚 API Documentation

The interactive documentation (Swagger UI) is available at:
- `http://localhost:8000/apidocs/` (Gunicorn)
- `http://localhost:5432/apidocs/` (Flask)

---

## 🔑 Main Endpoints

### GET /extractor
Returns raw data obtained through web scraping.

**Query Parameters:**
- `year` (optional): Year to collect data (default: current year)

**Required Headers:**
- `x-api-key`: Your API key

### GET /download
Returns processed and structured data in a compressed CSV file (.zip).

**Query Parameters:**
- `year` (optional): Year to collect data (default: current year)

**Required Headers:**
- `x-api-key`: Your API key

---

## 🔒 Security

- API Key authentication
- CORS configuration for allowed origins
- Environment variable validation

---

## 🧱 Architecture Diagram

![image](https://github.com/user-attachments/assets/00e70a17-87e1-4580-a1de-a643adf87ee2)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the [MIT License](LICENSE)

---

## ✒️ Authors

- **Gustavo Imbelloni**  
  [GitHub](https://github.com/gustavoimbelloni) · [LinkedIn](https://www.linkedin.com/in/gustavoimbelloni/)

- **Patrick Meirelles**  
  [GitHub](https://github.com/PatrickMeirelles) · [LinkedIn](https://www.linkedin.com/in/patrick-meirelles/)

- **Raíssa Campos dos Santos**  
  [GitHub](https://github.com/raissacsantos) · [LinkedIn](https://www.linkedin.com/in/ra%C3%ADssa-campos-dos-santos-51780625a/)

- **Vitor Nogueira Domingos**  
  [GitHub](https://github.com/vitornogueirad) · [LinkedIn](https://www.linkedin.com/in/vitor-nogueira-domingos/)

- **Vitor Crispim**  
  [GitHub](https://github.com/vtCrispim) · [LinkedIn](https://www.linkedin.com/in/vitor-crispim-7b3481179/)

---

## 📄 Notes

- Data is available until 2023
- API allows requests only from authorized origins (e.g., `localhost:3000`, `tech-challange-front.onrender.com`)
